# RAG + GPT (Retrieval-Augmented Generation) 시스템

이 프로젝트는 마크다운 파일들을 처리하여 ChromaDB 벡터 데이터베이스를 구축하고, OpenAI 임베딩을 사용하여 의미적 검색을 수행한 후, GPT를 통해 자연스러운 답변을 생성하는 완전한 RAG 시스템입니다.

## 주요 기능

- **마크다운 전처리**: 특수기호, 수식, 링크 등을 제거하여 깔끔한 텍스트로 변환
- **청크 분할**: 긴 문서를 의미 있는 단위로 분할
- **벡터 임베딩**: OpenAI의 text-embedding-ada-002 모델 사용
- **벡터 저장소**: ChromaDB를 사용한 효율적인 벡터 저장 및 검색
- **의미적 검색**: 쿼리와 유사한 문서 청크를 검색
- **GPT 답변 생성**: 검색 결과를 바탕으로 자연스러운 답변 생성
- **대화형 채팅**: 실시간 질의응답 인터페이스

## 설치 및 설정

### 1. 의존성 설치

```bash
uv sync
```

### 2. 환경변수 설정

`.env` 파일을 생성하고 OpenAI API 키를 설정하세요:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 사용법

### 1. 벡터 데이터베이스 구축

`data/raw` 디렉토리의 마크다운 파일들을 처리하여 벡터 데이터베이스를 구축합니다:

```bash
python rag/build_vectordb.py
```

### 2. RAG + GPT 대화형 채팅

구축된 벡터 데이터베이스를 사용하여 GPT와 함께 대화형 채팅을 수행합니다:

```bash
python rag/chat_demo.py
```

### 3. 검색 데모 실행 (기본 RAG만)

벡터 데이터베이스를 사용하여 기본 검색을 수행합니다:

```bash
python rag/search_demo.py
```

### 4. 프로그래밍 방식 사용

```python
from rag.rag_gpt_system import RAGGPTSystem

# RAG + GPT 시스템 초기화
rag_gpt = RAGGPTSystem()

# 질문에 대한 답변 생성
result = rag_gpt.ask("강화학습이란 무엇인가요?", n_results=3)

# 답변 출력
print(f"질문: {result['query']}")
print(f"답변: {result['answer']}")

# 참고 문서 출력
for i, search_result in enumerate(result['search_results'], 1):
    print(f"참고 {i}: {search_result['metadata']['file_name']}")
```

또는 기본 RAG만 사용:

```python
from rag import RAGSystem

# RAG 시스템 초기화
rag = RAGSystem()

# 벡터 데이터베이스 구축
rag.build_vector_database()

# 검색 수행
results = rag.search("강화학습이란 무엇인가요?", n_results=3)

# 결과 출력
for result in results:
    print(f"파일: {result['metadata']['file_name']}")
    print(f"내용: {result['document'][:200]}...")
    print(f"유사도: {1 - result['distance']:.4f}")
    print("-" * 50)
```

## 시스템 구조

```
rag/
├── __init__.py              # 패키지 초기화
├── vector_store.py         # ChromaDB 벡터 저장소 관리
├── rag_system.py           # 통합 RAG 시스템
├── rag_gpt_system.py       # RAG + GPT 결합 시스템
├── build_vectordb.py       # 벡터 DB 구축 스크립트
├── chat_demo.py            # RAG + GPT 대화형 채팅
└── README.md               # 이 파일
```

## 마크다운 전처리 기능

`MarkdownProcessor` 클래스는 다음과 같은 전처리를 수행합니다:

- **HTML 태그 제거**: 마크다운을 HTML로 변환 후 텍스트만 추출
- **마크다운 특수문자 제거**: `#*_` 등의 마크다운 문법 제거
- **수식 제거**: LaTeX 수식 (`$...$`, `$$...$$`) 제거
- **링크 정리**: `[텍스트](URL)` 형태를 텍스트만 남김
- **이미지 제거**: `![alt](URL)` 형태 완전 제거
- **코드 블록 제거**: 인라인 코드와 코드 블록 제거
- **YAML front matter 제거**: 문서 상단의 메타데이터 제거
- **공백 정리**: 연속된 공백과 줄바꿈 정리

## 청크 분할 전략

- **문단 단위 분할**: `\n\n`을 기준으로 문단을 구분
- **최대 크기 제한**: 기본 1000자 이하로 청크 크기 제한
- **의미 보존**: 문단의 경계를 유지하여 의미적 일관성 확보

## 벡터 저장소 정보

- **저장 경로**: `data/vectordb/`
- **컬렉션명**: `markdown_documents`
- **임베딩 모델**: OpenAI text-embedding-ada-002
- **메타데이터**: 파일명, 청크 인덱스, 소스 정보 등 포함

## GPT 모델 정보

- **기본 모델**: gpt-3.5-turbo
- **온도**: 0.3 (일관된 답변을 위해)
- **최대 토큰**: 1000 (기본값)
- **프롬프트**: 검색 결과를 바탕으로 한 구조화된 프롬프트

## 주의사항

1. **API 비용**: OpenAI 임베딩 API와 GPT API 사용 시 비용이 발생할 수 있습니다.
2. **파일 크기**: 대용량 마크다운 파일의 경우 처리 시간이 오래 걸릴 수 있습니다.
3. **메모리 사용량**: 많은 문서를 처리할 때 충분한 메모리가 필요합니다.
4. **토큰 제한**: GPT 모델의 토큰 제한으로 인해 긴 문서는 청크로 분할됩니다.

## 문제 해결

### OpenAI API 키 오류
```
오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.
```
- `.env` 파일에 올바른 API 키가 설정되어 있는지 확인하세요.

### 벡터 데이터베이스가 비어있음
```
벡터 데이터베이스가 비어있습니다.
```
- `python rag/build_vectordb.py`를 먼저 실행하여 데이터베이스를 구축하세요.

### 의존성 오류
```
ModuleNotFoundError: No module named 'chromadb'
```
- `uv sync`를 실행하여 의존성을 설치하세요. 