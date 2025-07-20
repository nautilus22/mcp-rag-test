#!/usr/bin/env python3
"""
RAG 검색 데모 스크립트

이 스크립트는 구축된 벡터 데이터베이스를 사용하여
사용자 쿼리에 대한 검색을 수행합니다.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from rag import RAGSystem

load_dotenv()


def print_search_results(results):
    """검색 결과를 보기 좋게 출력합니다."""
    if not results:
        print("검색 결과가 없습니다.")
        return
    
    print(f"\n=== 검색 결과 ({len(results)}개) ===")
    
    for i, result in enumerate(results, 1):
        print(f"\n--- 결과 {i} ---")
        print(f"파일: {result['metadata']['file_name']}")
        print(f"청크 인덱스: {result['metadata']['chunk_index'] + 1}/{result['metadata']['total_chunks']}")
        print(f"유사도 점수: {1 - result['distance']:.4f}")
        print(f"내용:")
        print(f"{result['document'][:300]}...")
        print("-" * 50)


def main():
    """메인 실행 함수"""
    print("=== RAG 검색 데모 ===")
    
    # OpenAI API 키 확인
    if not os.getenv("OPENAI_API_KEY"):
        print("오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        return False
    
    # RAG 시스템 초기화
    try:
        rag_system = RAGSystem()
        print("RAG 시스템이 초기화되었습니다.")
    except Exception as e:
        print(f"RAG 시스템 초기화 실패: {e}")
        return False
    
    # 벡터 데이터베이스 정보 확인
    collection_info = rag_system.get_collection_info()
    if not collection_info or collection_info.get('document_count', 0) == 0:
        print("벡터 데이터베이스가 비어있습니다.")
        print("먼저 'python rag/build_vectordb.py'를 실행하여 데이터베이스를 구축해주세요.")
        return False
    
    print(f"벡터 데이터베이스 정보:")
    print(f"  - 저장된 문서 수: {collection_info['document_count']}")
    print(f"  - 저장 경로: {collection_info['persist_directory']}")
    
    # 대화형 검색 루프
    print("\n검색을 시작합니다. 'quit' 또는 'exit'를 입력하면 종료됩니다.")
    
    while True:
        try:
            query = input("\n검색어를 입력하세요: ").strip()
            
            if query.lower() in ['quit', 'exit', '종료']:
                print("검색을 종료합니다.")
                break
            
            if not query:
                print("검색어를 입력해주세요.")
                continue
            
            # 검색 실행
            results = rag_system.search(query, n_results=3)
            print_search_results(results)
            
        except KeyboardInterrupt:
            print("\n\n검색을 종료합니다.")
            break
        except Exception as e:
            print(f"검색 중 오류 발생: {e}")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 