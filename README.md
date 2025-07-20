# MCP & RAG 프로젝트

한국 위키피디아 AI/ML 문서를 활용한 MCP 서버와 RAG 시스템의 독립적 구현 프로젝트입니다.

## 🎯 프로젝트 목표

- **직접 질문**: "딥러닝이 뭐야?"
- **비교 질문**: "CNN과 RNN의 차이는?"
- **추론 질문**: "GPT가 transformer 기반인 이유는?"
- **연관 질문**: "AlphaGo와 관련된 기술들은?"

위 질문들에 대해 **MCP**와 **RAG** 방식의 성능을 비교 테스트합니다.

## 📂 프로젝트 구조

- **shared/**: 공통 데이터 파싱 및 처리 모듈
- **rag/**: 단계별 스크립트 기반 RAG 시스템
- **mcp_server/**: Cursor/Claude 연동용 MCP 서버
- **data/**: 위키 데이터 및 벡터 DB 저장소
- **scripts/**: 환경 설정 및 실행 스크립트
- **docs/**: 사용 가이드 및 문서

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. API 키 설정
cp .env.example .env
# .env 파일에서 OPENAI_API_KEY 설정

# 또는 환경변수로 직접 설정
export OPENAI_API_KEY='your-api-key-here'
```

### 2. 위키피디아 데이터 다운로드

```bash
# AI/ML 관련 한국 위키피디아 문서를 크롤링하고 GPT로 요약
python scripts/download_wiki_data.py
```

이 명령으로 다음이 생성됩니다:
- `data/raw/aiml/`: 상세한 파일명의 원본 문서들
- `data/mcp_docs/`: MCP용 간단한 파일명의 문서들

### 3-A. RAG 시스템 사용

```bash
# 단계별 실행
python rag/scripts/step1_prepare_data.py      # 데이터 준비 및 전처리
python rag/scripts/step2_build_vectordb.py    # 벡터 DB 구축  
python rag/scripts/step3_setup_pipeline.py    # RAG 파이프라인 설정
python rag/scripts/step4_validate.py          # 파이프라인 검증

# 또는 전체 단계 한번에 실행
python rag/scripts/run_all_steps.py

# 쿼리 실험 (노트북 사용)
jupyter notebook rag/notebooks/query_experiments.ipynb

# 성능 분석 (선택사항)
jupyter notebook rag/notebooks/performance_analysis.ipynb
```

### 3-B. MCP 서버 사용

```bash
# 서버 실행
python scripts/run_mcp_server.py

# Cursor에서 연결
# Settings > Extensions > MCP > Add Server: localhost:8000

# Claude Desktop에서 연결  
# ~/.claude_desktop_config.json 파일 수정
```

## 📋 생성되는 파일 예시

### RAG용 파일 (data/raw/aiml/)
```
딥 러닝/Deep Learning/신경망을 여러 층으로 쌓아 복잡한 패턴을 학습하는 기술.txt
합성곱 신경망/CNN/이미지 인식에 특화된 딥러닝 모델로 필터를 사용해 특징 추출.txt
```

### MCP용 파일 (data/mcp_docs/)
```
딥러닝.txt
cnn.txt  
rnn.txt
gpt.txt
```

## 🔄 워크플로우

### RAG 방식
1. 문서를 벡터화하여 DB에 저장
2. 쿼리와 유사한 문서 조각 검색
3. 검색된 컨텍스트로 LLM 답변 생성

### MCP 방식  
1. 질문 키워드 분석
2. 관련 txt 파일 직접 접근
3. 파일 내용을 컨텍스트로 즉시 답변

## 🛠️ 주요 기능

- ✅ **한국 위키피디아 크롤링**: AI/ML 관련 11개 문서
- ✅ **GPT 자동 요약**: MCP 파일명 최적화
- ✅ **RAG 파이프라인**: 단계별 자동 구축  
- ✅ **MCP 서버**: IDE/AI 도구 연동
- ✅ **성능 비교**: 동일 질문에 대한 답변 품질 테스트

## 📊 테스트 질문 목록

1. **딥러닝이 뭐야?** (직접 질문)
2. **CNN과 RNN의 차이는?** (비교 질문)  
3. **GPT가 transformer 기반인 이유는?** (추론 질문)
4. **AlphaGo와 관련된 기술들은?** (연관 질문)

## 🔍 키워드 커버리지

| 키워드 | 한국어 위키 | 설명 |
|--------|-------------|------|
| 인공지능 | ✅ | AI 기본 개념 |
| 딥러닝 | ✅ | 신경망 다층 구조 |
| CNN | ✅ | 합성곱 신경망 |
| RNN | ✅ | 순환 신경망 |
| Transformer | ✅ | 어텐션 메커니즘 |
| GPT | ✅ | 생성형 언어모델 |
| AlphaGo | ✅ | 강화학습 사례 |
| ... | ... | ... |

## 📖 추가 문서

- [RAG 사용 가이드](docs/rag_usage.md)
- [MCP 설정 가이드](docs/mcp_setup.md)  
- [데이터 포맷 설명](docs/data_format.md)
