#!/usr/bin/env python3
"""
벡터 데이터베이스 구축 스크립트

이 스크립트는 data/raw 디렉토리의 마크다운 파일들을 처리하여
ChromaDB 벡터 데이터베이스를 구축합니다.
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


def main():
    """메인 실행 함수"""
    print("=== RAG 벡터 데이터베이스 구축 ===")
    
    # OpenAI API 키 확인
    if not os.getenv("OPENAI_API_KEY"):
        print("오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        print("환경변수를 설정하거나 .env 파일을 생성해주세요.")
        return False
    
    # RAG 시스템 초기화
    try:
        rag_system = RAGSystem()
        print("RAG 시스템이 초기화되었습니다.")
    except Exception as e:
        print(f"RAG 시스템 초기화 실패: {e}")
        return False
    
    # 기존 데이터베이스 정보 확인
    collection_info = rag_system.get_collection_info()
    if collection_info and collection_info.get('document_count', 0) > 0:
        print(f"기존 벡터 데이터베이스 발견: {collection_info['document_count']}개 문서")
        response = input("기존 데이터를 삭제하고 새로 구축하시겠습니까? (y/N): ")
        if response.lower() == 'y':
            rag_system.reset_database()
        else:
            print("작업을 취소했습니다.")
            return True
    
    # 벡터 데이터베이스 구축
    print("\n벡터 데이터베이스 구축을 시작합니다...")
    success = rag_system.build_vector_database()
    
    if success:
        print("\n=== 구축 완료 ===")
        print("벡터 데이터베이스가 성공적으로 구축되었습니다.")
        
        # 최종 통계 출력
        final_info = rag_system.get_collection_info()
        if final_info:
            print(f"저장된 문서 수: {final_info['document_count']}")
            print(f"저장 경로: {final_info['persist_directory']}")
        
        return True
    else:
        print("\n=== 구축 실패 ===")
        print("벡터 데이터베이스 구축에 실패했습니다.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 