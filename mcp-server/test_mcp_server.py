#!/usr/bin/env python3
"""
MCP RAG Server 테스트 스크립트
서버의 두 가지 주요 기능을 테스트합니다.
"""

import asyncio
import sys
from pathlib import Path

# 서버 모듈 임포트
try:
    from mcp_rag_server import get_all_documents, calculate_relevance_score, extract_relevant_content
except ImportError:
    print("❌ mcp_rag_server.py를 찾을 수 없습니다.")
    sys.exit(1)

async def test_search_functionality():
    """파일 검색 기능 테스트"""
    print("🔍 파일 검색 기능 테스트")
    print("-" * 50)
    
    # 1. 문서 로드 테스트
    documents = get_all_documents()
    print(f"📁 발견된 문서 수: {len(documents)}")
    
    if not documents:
        print("⚠️  ../data/raw/ 폴더에 문서가 없습니다.")
        print("   위키피디아 크롤링을 먼저 실행하거나 테스트 파일을 추가해주세요.")
        return False
    
    # 문서 목록 출력
    print("\n📋 사용 가능한 문서들:")
    for i, doc in enumerate(documents[:10], 1):  # 최대 10개만 표시
        print(f"   {i}. {doc['title']} ({doc['size']} bytes)")
    
    if len(documents) > 10:
        print(f"   ... 외 {len(documents) - 10}개")
    
    # 2. 관련성 점수 테스트
    print(f"\n🎯 관련성 점수 테스트")
    test_queries = [
        "딥러닝", "인공지능", "머신러닝", "신경망", 
        "트랜스포머", "CNN", "RNN", "강화학습"
    ]
    
    for query in test_queries:
        print(f"\n질문: '{query}'")
        scored_docs = []
        
        for doc in documents:
            score = calculate_relevance_score(query, doc["title"])
            if score > 0.1:
                scored_docs.append((score, doc))
        
        scored_docs.sort(key=lambda x: x[0], reverse=True)
        
        if scored_docs:
            print("  관련 문서:")
            for score, doc in scored_docs[:3]:
                print(f"    - {doc['title']}: {score:.2f}")
        else:
            print("  관련 문서 없음")
    
    return True

async def test_content_extraction():
    """내용 추출 기능 테스트"""
    print("\n\n📖 내용 추출 기능 테스트")
    print("-" * 50)
    
    documents = get_all_documents()
    
    if not documents:
        print("⚠️  테스트할 문서가 없습니다.")
        return False
    
    # 첫 번째 문서로 테스트
    test_doc = documents[0]
    test_queries = ["정의", "특징", "원리", "방법", "장점", "단점"]
    
    print(f"📄 테스트 문서: {test_doc['title']}")
    
    for query in test_queries:
        print(f"\n질문: '{query}'")
        try:
            content = extract_relevant_content(test_doc['path'], query, max_lines=10)
            if content:
                # 내용을 짧게 표시 (처음 200자만)
                preview = content[:200].replace('\n', ' ')
                if len(content) > 200:
                    preview += "..."
                print(f"  추출된 내용: {preview}")
            else:
                print("  관련 내용 없음")
        except Exception as e:
            print(f"  ❌ 오류: {e}")
    
    return True

async def test_edge_cases():
    """엣지 케이스 테스트"""
    print("\n\n🧪 엣지 케이스 테스트")
    print("-" * 50)
    
    # 1. 빈 질문
    print("1. 빈 질문 테스트")
    score = calculate_relevance_score("", "인공지능")
    print(f"   빈 질문 점수: {score}")
    
    # 2. 매우 긴 질문
    print("2. 긴 질문 테스트")
    long_query = "인공지능과 머신러닝 그리고 딥러닝의 차이점에 대해 알고 싶습니다 특히 신경망과 관련된 내용"
    score = calculate_relevance_score(long_query, "인공지능")
    print(f"   긴 질문 점수: {score}")
    
    # 3. 특수 문자 포함 질문
    print("3. 특수 문자 테스트")
    special_query = "AI/ML 기술이란???"
    score = calculate_relevance_score(special_query, "인공지능")
    print(f"   특수 문자 점수: {score}")
    
    # 4. 존재하지 않는 파일 테스트
    print("4. 존재하지 않는 파일 테스트")
    fake_path = Path("nonexistent_file.md")
    content = extract_relevant_content(fake_path, "테스트", max_lines=5)
    print(f"   결과: {content[:100]}...")
    
    return True

async def main():
    """메인 테스트 함수"""
    print("🚀 MCP RAG Server 테스트 시작")
    print("=" * 60)
    
    # 의존성 체크
    try:
        from fastmcp import FastMCP
        print("✅ FastMCP 의존성 확인됨")
    except ImportError:
        print("❌ FastMCP 패키지가 설치되지 않았습니다.")
        print("   uv add fastmcp 명령으로 설치해주세요.")
        return
    
    # 데이터 디렉토리 체크
    data_dir = Path("../data/raw")
    if not data_dir.exists():
        print(f"⚠️  데이터 디렉토리가 없습니다: {data_dir}")
        print("   ../data/raw/ 폴더를 생성하고 문서를 추가해주세요.")
        return
    
    # 테스트 실행
    success = True
    
    try:
        success &= await test_search_functionality()
        success &= await test_content_extraction()
        success &= await test_edge_cases()
        
        print("\n" + "=" * 60)
        if success:
            print("🎉 모든 테스트가 성공적으로 완료되었습니다!")
            print("\n다음 명령으로 MCP 서버를 실행할 수 있습니다:")
            print("   uv run mcp_rag_server.py")
        else:
            print("⚠️  일부 테스트에서 문제가 발견되었습니다.")
            
    except Exception as e:
        print(f"\n❌ 테스트 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main()) 