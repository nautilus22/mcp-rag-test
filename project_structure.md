# MCP & RAG 프로젝트 - 독립적인 구현

## 📂 프로젝트 구조

```
mcp-rag/
├── shared/                     # 🔄 공통 모듈
│   ├── __init__.py
│   ├── data_parser.py         # 한국 위키 크롤링 및 파싱
│   ├── text_processor.py      # 텍스트 전처리 유틸리티
│   └── config.py              # 공통 설정
├── rag/                       # 🔍 RAG 구현 (독립 실행)
│   ├── __init__.py
│   ├── src/
│   │   ├── __init__.py
│   │   ├── vector_store.py    # 벡터 DB 관리
│   │   ├── retriever.py       # 문서 검색기
│   │   ├── generator.py       # 답변 생성기
│   │   ├── pipeline.py        # RAG 파이프라인
│   │   └── evaluator.py       # 성능 평가 도구
│   ├── scripts/
│   │   ├── step1_prepare_data.py    # 1단계: 데이터 준비 및 전처리
│   │   ├── step2_build_vectordb.py  # 2단계: 벡터 DB 구축
│   │   ├── step3_setup_pipeline.py  # 3단계: RAG 파이프라인 설정
│   │   ├── step4_validate.py        # 4단계: 파이프라인 검증
│   │   └── run_all_steps.py         # 전체 단계 자동 실행
│   ├── notebooks/
│   │   ├── query_experiments.ipynb  # 🎯 쿼리 실험 및 결과 분석
│   │   └── performance_analysis.ipynb # 성능 분석 및 시각화
│   ├── config/
│   │   ├── __init__.py
│   │   └── rag_config.py      # RAG 시스템 설정
│   └── requirements_rag.txt   # RAG 전용 의존성
├── mcp_server/                # 🔌 MCP 서버 (Cursor/Claude 연결)
│   ├── __init__.py
│   ├── server.py              # MCP 서버 메인
│   ├── tools/                 # MCP 도구들
│   │   ├── __init__.py
│   │   ├── document_reader.py # 문서 읽기 도구
│   │   ├── search_tool.py     # 검색 도구
│   │   └── knowledge_tool.py  # 지식 검색 도구
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── file_handler.py    # 파일 처리
│   │   └── search_handler.py  # 검색 처리
│   ├── config/
│   │   ├── __init__.py
│   │   └── mcp_config.py      # MCP 서버 설정
│   └── requirements_mcp.txt   # MCP 전용 의존성
├── data/                      # 📁 데이터 저장소
│   ├── raw/                   # 원본 위키 데이터
│   │   └── aiml/             # AI/ML 관련 문서들
│   ├── processed/             # 전처리된 데이터
│   │   ├── chunks/           # 문서 청크들
│   │   └── metadata/         # 메타데이터
│   ├── vectordb/             # RAG용 벡터 데이터베이스
│   └── mcp_docs/             # MCP용 텍스트 파일들
├── scripts/                   # 🚀 실행 스크립트들
│   ├── download_wiki_data.py  # 위키 데이터 다운로드
│   ├── setup_all.py          # 전체 환경 설정
│   ├── run_mcp_server.py     # MCP 서버 실행
│   └── test_setup.py         # 설정 테스트
├── docs/                     # 📚 문서화
│   ├── rag_usage.md          # RAG 사용 가이드
│   ├── mcp_setup.md          # MCP 설정 가이드
│   └── data_format.md        # 데이터 포맷 설명
├── requirements.txt          # 기본 공통 의존성
├── pyproject.toml           # 프로젝트 설정
├── .env.example             # 환경변수 예시
└── README.md                # 프로젝트 전체 가이드
```

## 🔧 주요 컴포넌트 설명

### 1. 공통 모듈 (`shared/`)
- **데이터 파싱**: 한국 위키피디아 크롤링 및 파싱
- **텍스트 처리**: 공통 전처리 및 청킹
- **설정 관리**: 환경 변수 및 공통 설정

### 2. RAG 시스템 (`rag/`)
- **단계별 스크립트**: 데이터 준비→벡터DB 구축→파이프라인 설정→검증
- **자동화된 구축**: 전체 과정을 스크립트로 완전 자동화
- **쿼리 실험**: 노트북에서 실제 질문-답변 테스트만 진행
- **성능 분석**: 결과 시각화 및 평가 (선택적 노트북 사용)

### 3. MCP 서버 (`mcp_server/`)
- **표준 MCP 프로토콜**: JSON-RPC 기반 통신
- **도구 제공**: 문서 읽기, 검색, 지식 액세스 도구
- **Cursor/Claude 연결**: IDE 및 AI 어시스턴트와 직접 연동
- **실시간 파일 접근**: txt 파일 기반 즉시 응답

## 🛠️ 기술 스택

### 공통 (Shared)
- **BeautifulSoup**: 한국 위키 크롤링
- **pandas**: 데이터 처리 및 관리
- **python-dotenv**: 환경설정 관리

### RAG 시스템
- **LangChain**: RAG 파이프라인 구현
- **ChromaDB/FAISS**: 벡터 데이터베이스
- **sentence-transformers**: 임베딩 생성
- **OpenAI/Anthropic API**: LLM 서비스
- **Jupyter**: 대화형 개발 환경

### MCP 서버
- **mcp 라이브러리**: Model Context Protocol 공식 SDK
- **JSON-RPC 2.0**: MCP 표준 통신 프로토콜
- **asyncio**: 비동기 서버 처리
- **pathlib**: 파일 시스템 접근

## 📋 사용 시나리오

### RAG 워크플로우
```bash
# 🔧 단계별 스크립트 실행 (자동화)
python rag/scripts/step1_prepare_data.py      # 데이터 준비 및 전처리
python rag/scripts/step2_build_vectordb.py    # 벡터 DB 구축  
python rag/scripts/step3_setup_pipeline.py    # RAG 파이프라인 설정
python rag/scripts/step4_validate.py          # 파이프라인 검증

# 또는 전체 단계 한번에 실행
python rag/scripts/run_all_steps.py

# 🎯 쿼리 실험 (노트북 사용)
jupyter notebook rag/notebooks/query_experiments.ipynb

# 📊 성능 분석 (선택사항)
jupyter notebook rag/notebooks/performance_analysis.ipynb
```

### MCP 서버 사용
```bash
# 1. MCP 서버 실행
python scripts/run_mcp_server.py

# 2. Cursor에서 MCP 서버 연결
# - Settings > Extensions > MCP
# - Add server: localhost:8000

# 3. Claude Desktop 연결
# - ~/.claude_desktop_config.json 수정
```

## 🎯 독립성 및 공통점

### 독립적 운영
- **RAG**: Jupyter 노트북과 스크립트로 완전 독립 실행
- **MCP**: 별도 서버로 IDE/AI 도구와 연동
- **서로 의존성 없음**: 각각 별도로 개발 및 테스트 가능

### 공통 활용
- **데이터 파싱**: 동일한 위키 데이터 소스 사용
- **텍스트 처리**: 공통 전처리 파이프라인
- **설정 관리**: 환경변수 및 API 키 공유

## 🏗️ 아키텍처 다이어그램

```
📚 Korean Wikipedia (AI/ML Docs)
         │
         ▼
   ┌─────────────────┐
   │   shared/       │ 🔄 공통 모듈
   │ data_parser.py  │
   └─────────┬───────┘
             │
      ┌──────┴──────┐
      ▼             ▼
┌─────────────┐   ┌─────────────┐
│    RAG/     │   │ mcp_server/ │
│             │   │             │
│ scripts/    │   │   server.py │ 🔌 MCP 서버  
│ step1-4     │   │   tools/    │
│ (자동화)    │   │             │
│             │   └─────────────┘
│ notebooks/  │          │
│ (쿼리실험)  │          ▼
└─────────────┘   ┌─────────────┐
       │          │  Cursor/    │
       ▼          │  Claude     │ 💻 IDE/AI 도구
┌─────────────┐   │  Desktop    │
│  Vector DB  │   └─────────────┘
│ (ChromaDB)  │
└─────────────┘
```

### 특징:
- ✅ **완전 독립**: RAG와 MCP는 서로 의존하지 않음
- ✅ **공통 데이터**: 동일한 소스에서 데이터 파싱
- ✅ **효율적 워크플로우**: 
  - RAG: 스크립트로 자동 구축 → 노트북으로 쿼리 실험
  - MCP: 서버 실행 → IDE에서 AI 도구로 사용
- ✅ **단순하고 실용적**: 복잡한 웹 인터페이스 없이 목적에 집중 