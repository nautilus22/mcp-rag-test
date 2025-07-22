"""
위키피디아 데이터 다운로드 및 처리 스크립트
1. 크롤링한 원본 텍스트를 raw 폴더에 저장
2. MCP용 마크다운 처리된 파일을 mcp_docs에 저장  
3. RAG용 전처리된 파일을 rag_docs에 저장
"""

import sys
import os
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from utils.data_parser import WikiDataParser
from utils.markdown_processor import MarkdownProcessor
from utils.text_processor import TextProcessor


def main():
    """위키피디아 데이터 다운로드 및 처리 메인 실행"""
    
    print("=== 위키피디아 AI/ML 문서 다운로드 및 처리 ===")
    
    # OpenAI API 키 확인
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        print("다음 명령어로 API 키를 설정하세요:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # 위키피디아 문서 URL 목록
    wiki_data = {
        "인공지능": "https://ko.wikipedia.org/wiki/인공지능",
        "머신러닝": "https://ko.wikipedia.org/wiki/기계_학습", 
        "딥러닝": "https://ko.wikipedia.org/wiki/딥_러닝",
        "cnn": "https://ko.wikipedia.org/wiki/합성곱_신경망",
        "rnn": "https://ko.wikipedia.org/wiki/순환_신경망",
        "lstm": "https://ko.wikipedia.org/wiki/장단기_메모리",
        "gru": "https://ko.wikipedia.org/wiki/게이트_순환_유닛", 
        "transformer": "https://ko.wikipedia.org/wiki/트랜스포머_(기계_학습)",
        "gpt": "https://ko.wikipedia.org/wiki/GPT_(언어_모델)",
        "alphago": "https://ko.wikipedia.org/wiki/알파고",
        "강화학습": "https://ko.wikipedia.org/wiki/강화_학습"
    }
    
    try:
        # 1단계: 원본 텍스트 크롤링 및 저장
        print("\n📥 1단계: 원본 텍스트 크롤링 및 저장")
        raw_dir = project_root / "data" / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        
        raw_results = {}
        for i, (keyword, url) in enumerate(wiki_data.items(), 1):
            print(f"\n[{i}/{len(wiki_data)}] 크롤링 중: {keyword}")
            
            try:
                # 위키피디아 크롤링
                parser = WikiDataParser(api_key, str(raw_dir))
                title, content = parser.crawl_wikipedia_page(url)
                
                if content == "내용을 찾을 수 없습니다.":
                    print(f"  - 건너뜀: 내용 없음")
                    continue
                
                # 원본 텍스트를 .txt 파일로 저장
                raw_file_path = raw_dir / f"{keyword}.txt"
                with open(raw_file_path, 'w', encoding='utf-8') as f:
                    f.write(f"제목: {title}\n\n")
                    f.write(content)
                
                raw_results[keyword] = str(raw_file_path)
                print(f"  - 완료: {raw_file_path}")
                
            except Exception as e:
                print(f"  - 오류 발생: {e}")
                continue
        
        print(f"\n✅ 원본 텍스트 저장 완료: {len(raw_results)}개 파일")
        
        # 2단계: MCP용 마크다운 처리
        print("\n📝 2단계: MCP용 마크다운 처리")
        mcp_dir = project_root / "data" / "mcp_docs"
        mcp_dir.mkdir(parents=True, exist_ok=True)
        
        markdown_processor = MarkdownProcessor()
        mcp_results = {}
        
        for keyword, raw_path in raw_results.items():
            try:
                print(f"  - 처리 중: {keyword}")
                
                # 원본 텍스트 읽기
                with open(raw_path, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                
                # 마크다운 처리
                markdown_content = markdown_processor.process_for_mcp(raw_content)
                
                # MCP용 마크다운 파일 저장
                mcp_file_path = mcp_dir / f"{keyword}.md"
                with open(mcp_file_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                mcp_results[keyword] = str(mcp_file_path)
                print(f"    - 완료: {mcp_file_path}")
                
            except Exception as e:
                print(f"    - 오류 발생: {e}")
                continue
        
        print(f"✅ MCP용 마크다운 처리 완료: {len(mcp_results)}개 파일")
        
        # 3단계: RAG용 전처리
        print("\n🔧 3단계: RAG용 전처리")
        rag_dir = project_root / "data" / "rag_docs"
        rag_dir.mkdir(parents=True, exist_ok=True)
        
        text_processor = TextProcessor()
        rag_results = {}
        
        for keyword, raw_path in raw_results.items():
            try:
                print(f"  - 처리 중: {keyword}")
                
                # 원본 텍스트 읽기
                with open(raw_path, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                
                # RAG용 전처리
                processed_content = text_processor.process_for_rag(raw_content)
                
                # RAG용 텍스트 파일 저장
                rag_file_path = rag_dir / f"{keyword}.txt"
                with open(rag_file_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                rag_results[keyword] = str(rag_file_path)
                print(f"    - 완료: {rag_file_path}")
                
            except Exception as e:
                print(f"    - 오류 발생: {e}")
                continue
        
        print(f"✅ RAG용 전처리 완료: {len(rag_results)}개 파일")
        
        # 결과 요약
        print("\n" + "="*60)
        print("📋 처리 결과 요약")
        print("="*60)
        print(f"✅ 원본 텍스트: {len(raw_results)}개 파일 (data/raw/)")
        print(f"✅ MCP용 마크다운: {len(mcp_results)}개 파일 (data/mcp_docs/)")
        print(f"✅ RAG용 전처리: {len(rag_results)}개 파일 (data/rag_docs/)")
        
        print("\n📄 생성된 파일 목록:")
        for keyword in raw_results.keys():
            print(f"  • {keyword}:")
            print(f"    - 원본: data/raw/{keyword}.txt")
            print(f"    - MCP: data/mcp_docs/{keyword}.md")
            print(f"    - RAG: data/rag_docs/{keyword}.txt")
            
        print("\n🎉 모든 처리 완료!")
        
        # 다음 단계 안내
        print("\n" + "="*60)
        print("📖 다음 단계")
        print("="*60)
        print("1. RAG 시스템 구축:")
        print("   uv run rag/build_vectordb.py")
        print()
        print("2. RAG 채팅 데모:")
        print("   uv run rag/chat_demo.py")
        print()
        print("3. MCP 서버 실행:")
        print("   cd mcp-server")
        print("   uv run mcp_rag_server.py")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        print("문제가 지속되면 API 키와 네트워크 연결을 확인해주세요.")


if __name__ == "__main__":
    main() 