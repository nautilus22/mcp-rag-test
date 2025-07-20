#!/usr/bin/env python3
"""
MCP RAG Server - 위키피디아 문서 기반 질문 답변 시스템
사용자 질문에 대해 적합한 파일을 찾고 관련 내용을 추출하는 MCP 서버
"""

import os
import logging
from pathlib import Path
from typing import Any, List, Dict
import re
from fastmcp import FastMCP

# 로깅 설정 (stderr로 출력 - MCP 서버에서는 stdout 사용 금지)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# FastMCP 서버 초기화
mcp = FastMCP("rag-server")

# 상수 설정
DATA_DIR = Path("../data/raw")
SUPPORTED_EXTENSIONS = {".md", ".txt"}

def get_all_documents() -> List[Dict[str, Any]]:
    """
    data/raw 폴더에서 모든 문서 파일 정보를 가져옴
    
    Returns:
        문서 정보 리스트 [{"title": str, "path": Path, "size": int}, ...]
    """
    documents = []
    
    if not DATA_DIR.exists():
        logger.warning(f"데이터 디렉토리가 존재하지 않습니다: {DATA_DIR}")
        return documents
    
    for file_path in DATA_DIR.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            title = file_path.stem  # 확장자 제외한 파일명
            documents.append({
                "title": title,
                "path": file_path,
                "size": file_path.stat().st_size
            })
    
    logger.info(f"총 {len(documents)}개 문서를 발견했습니다.")
    return documents

def calculate_relevance_score(query: str, title: str) -> float:
    """
    질문과 파일 제목 간의 관련성 점수 계산
    
    Args:
        query: 사용자 질문
        title: 파일 제목
        
    Returns:
        관련성 점수 (0.0 ~ 1.0)
    """
    query_lower = query.lower()
    title_lower = title.lower()
    
    score = 0.0
    
    # 정확한 매칭 (가장 높은 점수)
    if title_lower in query_lower or query_lower in title_lower:
        score += 0.8
    
    # 단어별 매칭
    query_words = set(re.findall(r'\b\w+\b', query_lower))
    title_words = set(re.findall(r'\b\w+\b', title_lower))
    
    if query_words and title_words:
        common_words = query_words.intersection(title_words)
        word_score = len(common_words) / max(len(query_words), len(title_words))
        score += word_score * 0.6
    
    # 키워드 기반 매칭 (AI/ML 관련)
    ai_keywords = {
        'ai', 'artificial', 'intelligence', '인공지능', 'ai',
        'machine', 'learning', '머신러닝', '기계학습', 'ml',
        'deep', 'deeplearning', '딥러닝', 'neural', 'network', '신경망',
        'cnn', 'rnn', 'lstm', 'gru', 'transformer', 'gpt',
        'reinforcement', '강화학습', 'alphago', '알파고'
    }
    
    query_ai_words = set(query_lower.split()) & ai_keywords
    title_ai_words = set(title_lower.split()) & ai_keywords
    
    if query_ai_words and title_ai_words:
        score += 0.3
    
    return min(score, 1.0)

def extract_relevant_content(file_path: Path, query: str, max_lines: int = 50) -> str:
    """
    파일에서 질문과 관련된 내용을 추출
    
    Args:
        file_path: 파일 경로
        query: 사용자 질문
        max_lines: 최대 추출할 줄 수
        
    Returns:
        관련 내용 텍스트
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # YAML 메타데이터 제거
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()
        
        lines = content.split('\n')
        query_lower = query.lower()
        relevant_lines = []
        
        # 질문과 관련된 섹션 찾기
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # 헤더나 중요한 키워드가 포함된 줄 우선 선택
            if any(keyword in line_lower for keyword in query_lower.split()):
                # 해당 줄과 주변 맥락 포함
                start = max(0, i - 2)
                end = min(len(lines), i + 8)
                context = lines[start:end]
                relevant_lines.extend(context)
                
                if len(relevant_lines) >= max_lines:
                    break
        
        # 관련 내용이 없으면 파일 시작 부분 반환
        if not relevant_lines:
            relevant_lines = lines[:max_lines]
        
        return '\n'.join(relevant_lines[:max_lines])
        
    except Exception as e:
        logger.error(f"파일 읽기 오류 ({file_path}): {e}")
        return f"파일을 읽을 수 없습니다: {e}"

@mcp.tool()
async def search_files(query: str, max_results: int = 3) -> str:
    """
    사용자 질문에 대해 파일제목을 보고 적합한 파일들을 선택
    
    Args:
        query: 사용자의 질문이나 검색어
        max_results: 반환할 최대 파일 수 (기본값: 3)
    """
    logger.info(f"파일 검색 요청: '{query}'")
    
    documents = get_all_documents()
    
    if not documents:
        return "검색 가능한 문서가 없습니다. data/raw 폴더에 마크다운 파일을 추가해주세요."
    
    # 관련성 점수 계산 및 정렬
    scored_docs = []
    for doc in documents:
        score = calculate_relevance_score(query, doc["title"])
        if score > 0.1:  # 최소 관련성 임계값
            scored_docs.append((score, doc))
    
    # 점수 순으로 정렬
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    
    if not scored_docs:
        return f"'{query}'와 관련된 문서를 찾을 수 없습니다. 다른 검색어를 시도해보세요."
    
    # 최대 결과 수만큼 반환
    result_docs = scored_docs[:max_results]
    
    result = f"'{query}'에 대해 {len(result_docs)}개의 관련 문서를 찾았습니다:\n\n"
    
    for i, (score, doc) in enumerate(result_docs, 1):
        result += f"{i}. **{doc['title']}**\n"
        result += f"   - 관련성: {score:.2f}\n"
        result += f"   - 파일 크기: {doc['size']} bytes\n"
        result += f"   - 경로: {doc['path']}\n\n"
    
    result += "💡 이 파일들의 내용을 보려면 `get_relevant_content` 도구를 사용하세요."
    
    return result

@mcp.tool()
async def get_relevant_content(file_title: str, query: str, max_lines: int = 50) -> str:
    """
    특정 파일에서 질문과 관련된 내용을 추출
    
    Args:
        file_title: 파일 제목 (확장자 제외)
        query: 사용자의 질문
        max_lines: 추출할 최대 줄 수 (기본값: 50)
    """
    logger.info(f"내용 추출 요청: '{file_title}' 파일에서 '{query}' 관련 내용")
    
    documents = get_all_documents()
    
    # 파일 제목으로 문서 찾기
    target_file = None
    for doc in documents:
        if doc["title"].lower() == file_title.lower():
            target_file = doc["path"]
            break
    
    if not target_file:
        available_titles = [doc["title"] for doc in documents]
        return f"'{file_title}' 파일을 찾을 수 없습니다.\n사용 가능한 파일들: {', '.join(available_titles[:10])}"
    
    # 관련 내용 추출
    content = extract_relevant_content(target_file, query, max_lines)
    
    result = f"## {file_title}\n"
    result += f"**질문:** {query}\n\n"
    result += f"**관련 내용:**\n\n{content}\n\n"
    result += f"📄 파일 경로: {target_file}"
    
    return result

if __name__ == "__main__":
    logger.info("MCP RAG 서버를 시작합니다...")
    
    # 데이터 디렉토리 확인
    if not DATA_DIR.exists():
        logger.warning(f"데이터 디렉토리가 없습니다: {DATA_DIR}")
        logger.info("../data/raw/ 폴더를 생성하고 마크다운 파일을 추가해주세요.")
    
    # FastMCP 서버 실행
    mcp.run()