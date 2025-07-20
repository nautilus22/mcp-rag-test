from pathlib import Path
from typing import List, Dict, Any
from .markdown_processor import MarkdownProcessor
from .vector_store import VectorStore


class RAGSystem:
    """완전한 RAG 시스템 클래스"""
    
    def __init__(self, data_dir: str = "data/raw", vectordb_dir: str = "data/vectordb", preprocessed_dir: str = "data/preprocessed"):
        self.data_dir = Path(data_dir)
        self.vectordb_dir = Path(vectordb_dir)
        self.preprocessed_dir = Path(preprocessed_dir)
        
        # 컴포넌트 초기화
        self.markdown_processor = MarkdownProcessor(str(self.preprocessed_dir))
        self.vector_store = VectorStore(str(self.vectordb_dir))
    
    def build_vector_database(self) -> bool:
        """마크다운 파일들을 처리하여 벡터 데이터베이스를 구축합니다."""
        try:
            print("마크다운 파일 처리 중...")
            
            # 마크다운 파일 처리
            processed_documents = self.markdown_processor.process_directory(self.data_dir)
            
            if not processed_documents:
                print("처리할 마크다운 파일이 없습니다.")
                return False
            
            print(f"총 {len(processed_documents)}개의 마크다운 파일이 처리되었습니다.")
            
            # 벡터 저장소에 추가
            print("벡터 저장소에 문서 추가 중...")
            success = self.vector_store.add_documents(processed_documents)
            
            if success:
                print("벡터 데이터베이스 구축이 완료되었습니다.")
                self.print_statistics(processed_documents)
            else:
                print("벡터 데이터베이스 구축에 실패했습니다.")
            
            return success
            
        except Exception as e:
            print(f"벡터 데이터베이스 구축 중 오류 발생: {e}")
            return False
    
    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """쿼리를 검색하여 관련 문서를 반환합니다."""
        try:
            print(f"쿼리 검색 중: '{query}'")
            results = self.vector_store.search(query, n_results)
            
            if results:
                print(f"검색 결과: {len(results)}개의 문서를 찾았습니다.")
                return results
            else:
                print("검색 결과가 없습니다.")
                return []
                
        except Exception as e:
            print(f"검색 중 오류 발생: {e}")
            return []
    
    def print_statistics(self, processed_documents: List[Dict[str, Any]]):
        """처리된 문서들의 통계 정보를 출력합니다."""
        total_chunks = sum(len(doc['chunks']) for doc in processed_documents)
        total_files = len(processed_documents)
        total_original_size = sum(doc['metadata']['file_size'] for doc in processed_documents)
        total_preprocessed_size = sum(doc['metadata']['preprocessed_size'] for doc in processed_documents)
        
        print("\n=== 처리 통계 ===")
        print(f"총 파일 수: {total_files}")
        print(f"총 청크 수: {total_chunks}")
        print(f"원본 크기: {total_original_size:,} 문자")
        print(f"전처리 후 크기: {total_preprocessed_size:,} 문자")
        print(f"압축률: {((total_original_size - total_preprocessed_size) / total_original_size * 100):.1f}%")
        print(f"\n전처리된 텍스트 저장 경로: {self.preprocessed_dir}")
        print(f"벡터 DB 저장 경로: {self.vectordb_dir}")
        
        print("\n파일별 상세 정보:")
        for doc in processed_documents:
            original_size = doc['metadata']['file_size']
            preprocessed_size = doc['metadata']['preprocessed_size']
            compression_rate = ((original_size - preprocessed_size) / original_size * 100)
            print(f"  - {doc['file_name']}: {len(doc['chunks'])}개 청크, {original_size:,} → {preprocessed_size:,} 문자 ({compression_rate:.1f}% 압축)")
        
        # 벡터 저장소 정보
        collection_info = self.vector_store.get_collection_info()
        if collection_info:
            print(f"\n벡터 저장소 정보:")
            print(f"  - 컬렉션명: {collection_info['collection_name']}")
            print(f"  - 저장된 문서 수: {collection_info['document_count']}")
            print(f"  - 저장 경로: {collection_info['persist_directory']}")
    
    def get_collection_info(self) -> Dict[str, Any]:
        """벡터 저장소 정보를 반환합니다."""
        return self.vector_store.get_collection_info()
    
    def reset_database(self) -> bool:
        """벡터 데이터베이스를 초기화합니다."""
        try:
            print("벡터 데이터베이스 초기화 중...")
            success = self.vector_store.delete_collection()
            
            if success:
                # 새로운 벡터 저장소 인스턴스 생성
                self.vector_store = VectorStore(str(self.vectordb_dir))
                print("벡터 데이터베이스가 초기화되었습니다.")
            
            return success
            
        except Exception as e:
            print(f"데이터베이스 초기화 중 오류 발생: {e}")
            return False
    
    def process_single_file(self, file_path: Path) -> Dict[str, Any]:
        """단일 마크다운 파일을 처리합니다."""
        try:
            print(f"파일 처리 중: {file_path}")
            result = self.markdown_processor.process_markdown_file(file_path)
            
            if result:
                print(f"파일 처리 완료: {len(result['chunks'])}개 청크 생성")
                print(f"전처리된 텍스트 저장: {result['preprocessed_path']}")
                return result
            else:
                print("파일 처리에 실패했습니다.")
                return {}
                
        except Exception as e:
            print(f"파일 처리 중 오류 발생: {e}")
            return {} 