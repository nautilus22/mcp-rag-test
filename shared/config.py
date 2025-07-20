# 공통 설정 관리

import os
from pathlib import Path
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent

# 데이터 경로 설정
DATA_ROOT = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_ROOT / "raw" / "aiml"
PROCESSED_DATA_DIR = DATA_ROOT / "processed"
VECTOR_DB_DIR = DATA_ROOT / "vectordb"
MCP_DOCS_DIR = DATA_ROOT / "mcp_docs"

# API 설정
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 크롤링 설정
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 위키피디아 문서 목록
WIKI_DOCUMENTS = {
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

# 테스트 질문 목록
TEST_QUESTIONS = [
    "딥러닝이 뭐야?",
    "CNN과 RNN의 차이는?", 
    "GPT가 transformer 기반인 이유는?",
    "AlphaGo와 관련된 기술들은?"
] 