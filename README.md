# MCP & RAG 프로젝트

한국 위키피디아 AI/ML 문서를 활용한 MCP 서버와 RAG 시스템의 독립적 구현 프로젝트입니다.

## 🎯 프로젝트 목표

- **직접 질문**: "딥러닝이 뭐야?"
- **비교 질문**: "CNN과 RNN의 차이는?"
- **추론 질문**: "GPT가 transformer 기반인 이유는?"
- **연관 질문**: "AlphaGo와 관련된 기술들은?"

위 질문들에 대해 **MCP**와 **RAG** 방식의 성능을 비교 테스트합니다.

## 📂 프로젝트 구조

```
mcp-rag-test/
├── data/                    # 데이터 저장소
│   ├── raw/                # 원본 텍스트 파일들 (.txt)
│   ├── mcp_docs/           # MCP용 마크다운 파일들 (.md)
│   ├── rag_docs/           # RAG용 전처리된 텍스트 파일들 (.txt)
│   └── vectordb/          # ChromaDB 벡터 데이터베이스
├── mcp-server/            # MCP 서버 (Cursor/Claude 연동)
│   ├── mcp_rag_server.py  # MCP RAG 서버
│   ├── mcp_config.json    # MCP 설정 파일
│   └── test_mcp_server.py # MCP 서버 테스트
├── rag/                   # RAG 시스템
│   ├── __init__.py
│   ├── vector_store.py    # ChromaDB 벡터 저장소
│   ├── rag_system.py      # 기본 RAG 시스템
│   ├── rag_gpt_system.py  # RAG + GPT 결합 시스템
│   ├── build_vectordb.py  # 벡터 DB 구축 스크립트
│   └── chat_demo.py       # 대화형 채팅 데모
├── utils/                 # 유틸리티 및 데이터 처리
│   ├── __init__.py
│   ├── config.py          # 공통 설정
│   ├── data_parser.py     # 위키피디아 데이터 파서
│   ├── download_wiki_data.py # 위키 데이터 다운로드
│   ├── markdown_processor.py # 마크다운 전처리
│   └── text_processor.py  # 텍스트 프로세서
├── pyproject.toml         # uv 프로젝트 설정
├── uv.lock               # uv 의존성 잠금 파일
└── README.md             # 이 파일
```

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 1. uv 설치 (아직 설치하지 않은 경우)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 의존성 설치
uv sync

# 3. OpenAI API 키 설정
export OPENAI_API_KEY='your-api-key-here'
# 또는 .env 파일 생성 후 설정
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### 2. 위키피디아 데이터 다운로드

```bash
# AI/ML 관련 한국 위키피디아 문서를 크롤링하고 GPT로 요약
uv run utils/download_wiki_data.py
```

이 명령으로 다음이 생성됩니다:
- `data/raw/`: 원본 텍스트 파일들 (인공지능.txt, 딥러닝.txt, cnn.txt 등)
- `data/mcp_docs/`: MCP용 마크다운 파일들 (인공지능.md, 딥러닝.md, cnn.md 등)
- `data/rag_docs/`: RAG용 전처리된 텍스트 파일들 (인공지능.txt, 딥러닝.txt, cnn.txt 등)

### 3. RAG 시스템 구축

```bash
# 벡터 데이터베이스 구축
uv run rag/build_vectordb.py
```

이 과정에서:
- `data/rag_docs/`의 전처리된 텍스트 파일들이 청크로 분할되어 벡터화
- ChromaDB에 저장 (`data/vectordb/`)

### 4. RAG 시스템 사용

```bash
# 대화형 채팅 시작
uv run rag/chat_demo.py
```

예시 질문:
- "딥러닝이 뭐야?"
- "CNN과 RNN의 차이는?"
- "GPT가 transformer 기반인 이유는?"

### 5. MCP 서버 실행 (선택사항)

```bash
# MCP 서버 실행
cd mcp-server
uv run mcp_rag_server.py
```

**Cursor에서 연결:**
1. Cursor 설정 파일 열기: `~/.cursor/mcp.json`
2. 다음 설정 추가:
```json
{
  "mcpServers": {
    "rag-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/nautilus22/Work/LLM-Project/mcp-rag-test/mcp-server",
        "run",
        "mcp_rag_server.py"
      ]
    }
  }
}
```
3. Cursor 재시작

**Claude Desktop에서 연결:**
1. Claude Desktop 설정 파일 열기: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. 다음 설정 추가:
```json
{
  "mcpServers": {
    "rag-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/nautilus22/Work/LLM-Project/mcp-rag-test/mcp-server",
        "run",
        "mcp_rag_server.py"
      ]
    }
  }
}
```
3. Claude Desktop 재시작

**주의사항:**
- 경로는 절대 경로를 사용해야 합니다
- `uv` 명령어 경로가 다를 수 있습니다 (`which uv`로 확인)
- 서버가 실행 중이어야 합니다

## 📋 생성되는 파일 예시

### 원본 파일 (data/raw/)
```
인공지능.txt
딥러닝.txt
cnn.txt
rnn.txt
lstm.txt
gru.txt
transformer.txt
gpt.txt
alphago.txt
강화학습.txt
머신러닝.txt
```

### MCP용 파일 (data/mcp_docs/)
```
인공지능.md
딥러닝.md
cnn.md
rnn.md
lstm.md
gru.md
transformer.md
gpt.md
alphago.md
강화학습.md
머신러닝.md
```

### RAG용 파일 (data/rag_docs/)
```
인공지능.txt
딥러닝.txt
cnn.txt
rnn.txt
lstm.txt
gru.txt
transformer.txt
gpt.txt
alphago.txt
강화학습.txt
머신러닝.txt
```

## 🔄 워크플로우

### RAG 방식
1. 문서를 벡터화하여 ChromaDB에 저장
2. 쿼리와 유사한 문서 청크 검색
3. 검색된 컨텍스트로 GPT 답변 생성

### MCP 방식  
1. 질문 키워드 분석
2. 관련 md 파일 직접 접근
3. 파일 내용을 컨텍스트로 즉시 답변

## 🛠️ 주요 기능

- ✅ **한국 위키피디아 크롤링**: AI/ML 관련 11개 문서
- ✅ **GPT 자동 요약**: 문서 내용 최적화
- ✅ **마크다운 전처리**: 특수문자, 수식, 링크 제거
- ✅ **청크 분할**: 의미 있는 단위로 문서 분할
- ✅ **벡터 임베딩**: OpenAI text-embedding-ada-002 사용
- ✅ **ChromaDB 저장소**: 효율적인 벡터 저장 및 검색
- ✅ **RAG + GPT 결합**: 자연스러운 답변 생성
- ✅ **MCP 서버**: IDE/AI 도구 연동
- ✅ **대화형 채팅**: 실시간 질의응답 인터페이스

## 📊 테스트 질문 목록

1. **딥러닝이 뭐야?** (직접 질문)
2. **CNN과 RNN의 차이는?** (비교 질문)  
3. **GPT가 transformer 기반인 이유는?** (추론 질문)
4. **AlphaGo와 관련된 기술들은?** (연관 질문)

## 🔍 키워드 커버리지

| 키워드 | 한국어 위키 | 설명 |
|--------|-------------|------|
| 인공지능 | ✅ | AI 기본 개념 |
| 기계 학습 | ✅ | 머신러닝 기본 |
| 딥 러닝 | ✅ | 신경망 다층 구조 |
| 합성곱 신경망 | ✅ | CNN, 이미지 인식 |
| 순환 신경망 | ✅ | RNN, 시퀀스 처리 |
| 장단기 메모리 | ✅ | LSTM, 장기 의존성 |
| 게이트 순환 유닛 | ✅ | GRU, LSTM 대안 |
| 트랜스포머 | ✅ | 어텐션 메커니즘 |
| GPT | ✅ | 생성형 언어모델 |
| 알파고 | ✅ | 강화학습 사례 |
| 강화 학습 | ✅ | 강화학습 기본 |

## 🐛 문제 해결

### OpenAI API 키 오류
```bash
오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.
```
- `.env` 파일에 올바른 API 키가 설정되어 있는지 확인
- `export OPENAI_API_KEY='your-api-key-here'` 실행

### 벡터 데이터베이스가 비어있음
```bash
벡터 데이터베이스가 비어있습니다.
```
- `uv run rag/build_vectordb.py` 먼저 실행

### 의존성 오류
```bash
ModuleNotFoundError: No module named 'chromadb'
```
- `uv sync` 실행하여 의존성 설치

## 📖 추가 문서

- [RAG 시스템 상세 가이드](rag/README.md)
- [MCP 서버 설정 가이드](mcp-server/MCP_README.md)
- [프로젝트 구조 상세](project_structure.md)

## 🎉 완료!

이제 RAG 시스템을 사용하여 AI/ML 관련 질문에 대해 정확하고 상세한 답변을 받을 수 있습니다!
