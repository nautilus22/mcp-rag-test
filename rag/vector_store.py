import chromadb
from chromadb.config import Settings
from pathlib import Path
from typing import List, Dict, Any, Optional
import openai
import os
from dotenv import load_dotenv

load_dotenv()


class VectorStore:
    """ChromaDB를 사용한 벡터 저장소 관리 클래스"""
    
    def __init__(self, persist_directory: str = "data/vectordb"):
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(parents=True, exist_ok=True)
        
        # ChromaDB 클라이언트 초기화
        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        # OpenAI API 키 확인
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        
        # 컬렉션 생성 또는 가져오기
        self.collection = self.client.get_or_create_collection(
            name="markdown_documents",
            metadata={"description": "마크다운 문서 임베딩 저장소"}
        )
    
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """OpenAI API를 사용하여 텍스트를 임베딩합니다."""
        try:
            client = openai.OpenAI()
            response = client.embeddings.create(
                model="text-embedding-ada-002",
                input=texts
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            print(f"임베딩 생성 중 오류 발생: {e}")
            return []
    
    def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """문서들을 벡터 저장소에 추가합니다."""
        try:
            all_texts = []
            all_metadatas = []
            all_ids = []
            
            for doc in documents:
                file_name = doc['file_name']
                chunks = doc['chunks']
                
                for i, chunk in enumerate(chunks):
                    chunk_id = f"{file_name}_chunk_{i}"
                    all_ids.append(chunk_id)
                    all_texts.append(chunk)
                    all_metadatas.append({
                        'file_name': file_name,
                        'file_path': doc['file_path'],
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'source': 'markdown',
                        **doc['metadata']
                    })
            
            # 배치 크기 설정 (토큰 제한 고려)
            batch_size = 50
            total_added = 0
            
            for i in range(0, len(all_texts), batch_size):
                batch_texts = all_texts[i:i + batch_size]
                batch_metadatas = all_metadatas[i:i + batch_size]
                batch_ids = all_ids[i:i + batch_size]
                
                print(f"배치 {i//batch_size + 1} 처리 중... ({len(batch_texts)}개 청크)")
                
                # 임베딩 생성
                embeddings = self.get_embeddings(batch_texts)
                
                if not embeddings:
                    print(f"배치 {i//batch_size + 1} 임베딩 생성에 실패했습니다.")
                    continue
                
                # ChromaDB에 추가
                self.collection.add(
                    embeddings=embeddings,
                    documents=batch_texts,
                    metadatas=batch_metadatas,
                    ids=batch_ids
                )
                
                total_added += len(batch_texts)
            
            print(f"총 {total_added}개의 청크가 벡터 저장소에 추가되었습니다.")
            return total_added > 0
            
        except Exception as e:
            print(f"문서 추가 중 오류 발생: {e}")
            return False
    
    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """쿼리와 유사한 문서를 검색합니다."""
        try:
            # 쿼리 임베딩 생성
            query_embedding = self.get_embeddings([query])
            
            if not query_embedding:
                return []
            
            # 유사도 검색
            results = self.collection.query(
                query_embeddings=query_embedding,
                n_results=n_results,
                include=['documents', 'metadatas', 'distances']
            )
            
            # 결과 정리
            search_results = []
            for i in range(len(results['documents'][0])):
                search_results.append({
                    'document': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i]
                })
            
            return search_results
            
        except Exception as e:
            print(f"검색 중 오류 발생: {e}")
            return []
    
    def get_collection_info(self) -> Dict[str, Any]:
        """컬렉션 정보를 반환합니다."""
        try:
            count = self.collection.count()
            return {
                'collection_name': self.collection.name,
                'document_count': count,
                'persist_directory': str(self.persist_directory)
            }
        except Exception as e:
            print(f"컬렉션 정보 조회 중 오류 발생: {e}")
            return {}
    
    def delete_collection(self) -> bool:
        """컬렉션을 삭제합니다."""
        try:
            self.client.delete_collection(name=self.collection.name)
            print(f"컬렉션 '{self.collection.name}'이 삭제되었습니다.")
            return True
        except Exception as e:
            print(f"컬렉션 삭제 중 오류 발생: {e}")
            return False 