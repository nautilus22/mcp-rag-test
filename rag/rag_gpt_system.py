import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
import openai
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from rag import RAGSystem

load_dotenv()


class RAGGPTSystem:
    """RAG + GPT 결합 시스템"""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        # OpenAI API 키 확인
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        
        self.client = openai.OpenAI()
        self.model = model
        self.rag_system = RAGSystem()
    
    def create_prompt(self, query: str, search_results: List[Dict[str, Any]]) -> str:
        """검색 결과를 바탕으로 GPT 프롬프트를 생성합니다."""
        if not search_results:
            return f"질문: {query}\n\n답변: 제공된 문서에서 관련 정보를 찾을 수 없습니다."
        
        # 검색 결과를 정리
        context_parts = []
        for i, result in enumerate(search_results, 1):
            file_name = result['metadata']['file_name']
            chunk_index = result['metadata']['chunk_index'] + 1
            total_chunks = result['metadata']['total_chunks']
            content = result['document']
            similarity = 1 - result['distance']
            
            context_parts.append(f"[문서 {i}] {file_name} (청크 {chunk_index}/{total_chunks}, 유사도: {similarity:.3f})\n{content}")
        
        context = "\n\n".join(context_parts)
        
        prompt = f"""다음은 사용자의 질문과 관련된 문서 내용입니다. 이 정보를 바탕으로 정확하고 유용한 답변을 제공해주세요.

질문: {query}

관련 문서 내용:
{context}

위의 문서 내용을 바탕으로 질문에 답변해주세요. 다음 사항을 지켜주세요:
1. 제공된 문서 내용에 기반하여 답변하세요
2. 문서에 없는 내용은 추측하지 마세요
3. 명확하고 이해하기 쉽게 설명해주세요
4. 필요시 문서의 출처를 언급해주세요
5. 한국어로 답변해주세요

답변:"""
        
        return prompt
    
    def generate_answer(self, query: str, search_results: List[Dict[str, Any]], max_tokens: int = 1000) -> Dict[str, Any]:
        """GPT를 사용하여 답변을 생성합니다."""
        try:
            prompt = self.create_prompt(query, search_results)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "당신은 도움이 되는 AI 어시스턴트입니다. 제공된 문서 내용을 바탕으로 정확하고 유용한 답변을 제공해주세요."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.3
            )
            
            answer = response.choices[0].message.content.strip()
            
            return {
                'query': query,
                'answer': answer,
                'search_results': search_results,
                'model': self.model,
                'tokens_used': response.usage.total_tokens if hasattr(response, 'usage') else None
            }
            
        except Exception as e:
            print(f"답변 생성 중 오류 발생: {e}")
            return {
                'query': query,
                'answer': f"답변 생성 중 오류가 발생했습니다: {e}",
                'search_results': search_results,
                'model': self.model,
                'error': str(e)
            }
    
    def ask(self, query: str, n_results: int = 5, max_tokens: int = 1000) -> Dict[str, Any]:
        """질문을 받아서 RAG 검색 후 GPT로 답변을 생성합니다."""
        print(f"질문: {query}")
        print("검색 중...")
        
        # RAG 검색 수행
        search_results = self.rag_system.search(query, n_results)
        
        if not search_results:
            return {
                'query': query,
                'answer': "죄송합니다. 질문과 관련된 정보를 찾을 수 없습니다.",
                'search_results': [],
                'model': self.model
            }
        
        print(f"관련 문서 {len(search_results)}개를 찾았습니다. 답변을 생성 중...")
        
        # GPT로 답변 생성
        result = self.generate_answer(query, search_results, max_tokens)
        
        return result
    
    def print_answer(self, result: Dict[str, Any], show_sources: bool = True):
        """답변을 보기 좋게 출력합니다."""
        print(f"\n{'='*60}")
        print(f"질문: {result['query']}")
        print(f"{'='*60}")
        print(f"\n답변:\n{result['answer']}")
        
        if show_sources and result.get('search_results'):
            print(f"\n{'='*60}")
            print("참고 문서:")
            for i, search_result in enumerate(result['search_results'], 1):
                file_name = search_result['metadata']['file_name']
                chunk_index = search_result['metadata']['chunk_index'] + 1
                total_chunks = search_result['metadata']['total_chunks']
                similarity = 1 - search_result['distance']
                print(f"{i}. {file_name} (청크 {chunk_index}/{total_chunks}, 유사도: {similarity:.3f})")
        
        if result.get('tokens_used'):
            print(f"\n사용된 토큰: {result['tokens_used']}")
        
        print(f"{'='*60}")
    
    def interactive_chat(self):
        """대화형 채팅 모드를 시작합니다."""
        print("=== RAG + GPT 대화형 채팅 ===")
        print("질문을 입력하세요. 'quit', 'exit', '종료'를 입력하면 종료됩니다.")
        print("'sources off'를 입력하면 참고 문서 표시를 끌 수 있습니다.")
        print("'sources on'을 입력하면 참고 문서 표시를 켤 수 있습니다.")
        
        show_sources = True
        
        while True:
            try:
                query = input("\n질문: ").strip()
                
                if query.lower() in ['quit', 'exit', '종료']:
                    print("채팅을 종료합니다.")
                    break
                
                if query.lower() == 'sources off':
                    show_sources = False
                    print("참고 문서 표시가 꺼졌습니다.")
                    continue
                
                if query.lower() == 'sources on':
                    show_sources = True
                    print("참고 문서 표시가 켜졌습니다.")
                    continue
                
                if not query:
                    print("질문을 입력해주세요.")
                    continue
                
                # 답변 생성
                result = self.ask(query)
                self.print_answer(result, show_sources)
                
            except KeyboardInterrupt:
                print("\n\n채팅을 종료합니다.")
                break
            except Exception as e:
                print(f"오류 발생: {e}") 