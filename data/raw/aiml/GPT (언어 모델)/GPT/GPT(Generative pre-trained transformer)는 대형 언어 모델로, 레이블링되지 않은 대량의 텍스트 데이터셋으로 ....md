---
title: GPT (언어 모델)
type: 위키피디아 문서
format: markdown
---

# GPT (언어 모델)

- 지도 학습
- 비지도 학습
- 온라인 기계 학습
- 메타-학습
- 준지도 학습
- 자기 지도 학습
- 강화 학습
- 규칙 기반 기계 학습
- 뉴로모픽 엔지니어링
- 양자 기계 학습

- 분류
- 생성 모델
- 회귀 분석
- 클러스터 분석
- 차원 축
- 이상 탐지
- 데이터 정제
- AutoML
- 연관 규칙 학습
- 구조 기반 예측
- 특징 공학
- 특징 학습
- 순위 학습
- 문법 유도
- 온톨로지 학습
- 멀티모달 학습

- 결정 트리 학습법
- 앙상블 학습법 배깅 부스팅 랜덤 포레스트
- 최근접 이웃 탐색
- k-NN
- 선형 회귀
- 나이브 베이즈
- 인공신경망
- 로지스틱 회귀
- 퍼셉트론
- 상관 벡터 머신(RVM)
- 서포트 벡터 머신(SVM)

- 배깅
- 부스팅
- 랜덤 포레스트

- BIRCH
- CURE 알고리즘
- 계층적 군집화
- k-평균 알고리즘
- 퍼지 클러스터링
- 기댓값 최대화 알고리즘
- DBSCAN
- OPTICS
- 평균이동

- 인자 분석
- CCA
- 독립 성분 분석
- 선형 판별 분석
- 음수 미포함 행렬 분해
- 주성분 분석
- t-SNE

- 그래프 모형 베이즈 네트워크 조건부 무작위장 은닉 마르코프 모형
- 잠재 디리클레 할당

- 베이즈 네트워크
- 조건부 무작위장
- 은닉 마르코프 모형

- 무작위 표본 합의
- k-최근접 이웃 알고리즘
- 국소 특이점 요인
- 고립 포레스트

- 오토인코더
- 딥 러닝
- 순방향 신경망
- 순환 신경망 LSTM GRU
- 볼츠만 머신 제한된
- 생성적 적대 신경망
- 확산 모델
- 자기조직화 지도
- 합성곱 신경망 U-Net LeNet 알렉스넷 딥드림
- 신경장 신경 방사장 물리정보 신경망
- 트랜스포머 비전
- 맘바
- 스파이킹 신경망
- 멤트렌지스터
- 전기화학 RAM
- 다층 퍼셉트론

- LSTM
- GRU

- 제한된

- U-Net
- LeNet
- 알렉스넷
- 딥드림

- 신경 방사장
- 물리정보 신경망

- 비전

- Q 러닝
- SARSA
- 시간차 학습

- 액티브 러닝
- 크라우드소싱
- 휴먼인더루프
- RLHF

- 결정계수
- 혼동 행렬
- 러닝 커브
- 수신자 조작 특성

- 커널 메소드
- 편향-분산 트레이드오프
- 계산학습이론
- 경험적 위험 최소화
- PAC 러닝
- 통계적 학습이론
- VC 이론

- NeurIPS
- ICML
- ICLR
- ML
- JMLR

- 기계 학습 알고리즘 목록
- 기계 탈학습
- 지식 증류
- 유사도 학습
- 대조 학습

- v
- t
- e

**GPT**(Generative pre-trained transformer)는 미국의 [인공지능](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5) 단체 [오픈AI](https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%88AI)가 2018년 선보인 [대형 언어 모델](https://ko.wikipedia.org/wiki/%EB%8C%80%ED%98%95_%EC%96%B8%EC%96%B4_%EB%AA%A8%EB%8D%B8)(LLM)의 계열이며 GPT 모델들은 레이블링되지 않은 대량의 텍스트 데이터셋으로 미리 훈련되고 인간과 같은 문자를 생성할 수 있는 [변환기](https://ko.wikipedia.org/wiki/%EB%B3%80%ED%99%98%EA%B8%B0_(%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5)) 아키텍처에 기반한 [인공 신경망](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5_%EC%8B%A0%EA%B2%BD%EB%A7%9D)이다. 2023년 기준으로, 대부분의 LLM은 이러한 특징을 지니고 있으며 종종 GPT로 통칭한다.

OpenAI는 "GPT-n" 시리즈를 구성하기 위해 순차적으로 번호가 매겨진 매우 영향력 있는 GPT 기반 모델을 출시했다. 이들 각각은 증가된 크기(훈련 가능한 매개변수의 수) 및 훈련으로 인해 이전보다 훨씬 더 많은 능력을 발휘했다. 가장 최근인 GPT-4는 2023년 3월에 출시되었다. 이러한 모델은 지침을 따르도록 미세 조정된 모델을 포함하여 작업별 GPT 시스템의 기반이 되었으며, 이는 ChatGPT 챗봇 서비스를 지원한다.

"GPT"라는 용어는 다른 사람이 개발한 모델의 이름 또는 설명에도 자주 사용된다. 예를 들어 다른 GPT 기초 모델에는 EleutherAI에서 생성한 일련의 GPT-3에서 영감을 받은 모델과 최근 Cerebras에서 생성한 7개의 모델 시리즈가 포함된다. 또한 세일즈포스의 "EinsteinGPT"(CRM용) 및 블룸버그의 "BloombergGPT"(금융용)와 같이 다양한 산업 분야의 회사에서 해당 분야의 작업별 GPT를 개발했다.

### 역사

생성형 사전 훈련(Generative pre-training, GP)은 기계 학습 응용 프로그램에서 오랫동안 확립된 개념이었지만 변환기 아키텍처는 구글에서 발명한 2017년까지 사용할 수 없었다. 이러한 개발로 인해 2018년에는 BERT, 2019년에는 XLNet과 같은 대규모 언어 모델이 등장했다. 이것들은 사전 훈련된 변환기(PT)였지만 생성하도록 설계되지 않았다("인코더 전용"). 또한 그 무렵인 2018년에 OpenAI는 "생성적 사전 훈련에 의한 언어 이해 개선"이라는 제목의 기사를 발표하여 최초의 사전 훈련된 생성 변환기(GPT) 시스템을 도입했다.

변환기 기반 아키텍처 이전에 최고 성능의 신경 NLP(자연어 처리) 모델은 일반적으로 대량의 수동 레이블 지정 데이터에서 지도 학습을 사용했다. 감독 학습에 대한 의존도는 잘 주석이 없는 데이터 세트에 대한 사용을 제한했으며, 또한 매우 큰 언어 모델을 교육하는 데 엄청난 비용과 시간이 소요되었다.

대규모 생성 시스템을 만들기 위해 OpenAI가 채택한 준감독 접근 방식(처음에는 변환기 모델과 관련됨)에는 언어 모델링 목표를 사용하여 초기 매개변수를 설정하는 감독되지 않은 생성 "사전 훈련" 단계와 이러한 매개 변수를 대상 작업에 적용하기 위해 감독된 차별적 "미세 조정" 단계이다.

### 기초 모델

### 작업 특화 모델

기본 GPT 모델을 추가로 조정하여 특정 작업 및 주제 영역을 대상으로 하는 더 많은 대상 시스템을 생성할 수 있다. 이러한 적응 방법에는 추가 미세 조정(기초 모델에 대해 수행된 것 이상)과 특정 형태의 신속한 엔지니어링이 포함될 수 있다.

이에 대한 중요한 예는 지침을 따르도록 모델을 미세 조정하는 것이다. 2022년 1월 OpenAI는 기본 GPT-3 언어 모델에서 감독 교육과 인간 피드백으로부터 강화 학습(RLHF)을 조합하여 지침을 따르도록 미세 조정된 일련의 모델인 "InstructGPT"를 도입했다. 기본적인 기본 모델에 비해 더 높은 정확도, 부정적인/독성 감정이 적고 일반적으로 사용자 요구에 더 잘 부합하는 이점이 있다. 따라서 OpenAI는 이를 API 서비스 제공의 기반으로 사용하기 시작했다. 완전히 공개된 버전을 포함하여 다른 지침 조정 모델이 다른 사람들에 의해 출시되었다.

또 다른 (관련된) 종류의 작업별 모델은 인간과 유사한 대화에 참여하는 챗봇이다. 2022년 11월 OpenAI는 InstructGPT와 유사한 방식으로 훈련된 명령 조정 언어 모델로 구동되는 온라인 채팅 인터페이스인 ChatGPT를 출시했다. 그들은 RLHF를 사용하여 이 모델을 훈련시켰고 인간 AI 트레이너는 사용자와 AI를 모두 플레이하는 대화를 제공하고 이 새로운 대화 데이터 세트를 InstructGPT 데이터 세트와 혼합하여 챗봇에 적합한 대화 형식을 만들었다. 다른 주요 챗봇에는 현재 OpenAI의 GPT-4를 사용하는 마이크로소프트의 Bing Chat(OpenAI와 마이크로소프트 간의 보다 광범위한 긴밀한 협력의 일환으로)과 Google의 경쟁 챗봇 바드(처음에는 LaMDA 계열의 대화 훈련 언어 모델을 기반으로 하며 계획했다가 PalM으로 전환)가 포함된다.

GPT를 사용할 수 있는 또 다른 종류의 작업은 인간 사용자가 제공한 보다 일반적인 목표를 달성할 수 있도록 '자체'에 대한 일련의 프롬프트를 개발하는 것과 같이 자체 지침을 생성하는 메타 작업이다. 이것은 AI 에이전트로 알려져 있으며, 보다 구체적으로는 이전 자체 지침의 결과를 사용하여 후속 프롬프트를 형성하는 데 도움이 되기 때문에 재귀 에이전트라고 한다. 이것의 첫 번째 주요 예는 Auto-GPT(OpenAI의 GPT 모델을 사용함)였으며 이후 다른 것들도 개발되었다.

### 챗GPT-4.5의 튜링 검사 통과

미국 [캘리포니아 대학교 샌디에이고](https://ko.wikipedia.org/wiki/%EC%BA%98%EB%A6%AC%ED%8F%AC%EB%8B%88%EC%95%84_%EB%8C%80%ED%95%99%EA%B5%90_%EC%83%8C%EB%94%94%EC%97%90%EC%9D%B4%EA%B3%A0) 연구팀은 2025년에 [튜링 검사](https://ko.wikipedia.org/wiki/%ED%8A%9C%EB%A7%81_%EA%B2%80%EC%82%AC)에 대한 연구를 하였다. 심판이 사람과 인공지능과 동시에 대화하여 누가 사람인지 고르는 3자 튜링 검사에서 '게임과 인터넷 문화를 좋아하는 내성적인 10대 후반' 등의 가상 성격이 주어진 [GPT-4](https://ko.wikipedia.org/wiki/GPT-4).5는 참가자의 73%가 사람이라고 골랐고 실제 사람은 27%가 사람이라고 골랐다.

### 같이 보기

- Cyc
- 제미니 (언어 모델)

### 각주

1. ↑ 가 나 “Improving language understanding with unsupervised learning”. 《openai.com》 (미국 영어). 2023년 3월 18일에 원본 문서에서 보존된 문서. 2023년 3월 18일에 확인함.
2. ↑ 가 나 Haddad, Mohammed. “How does GPT-4 work and how can you start using it in ChatGPT?”. 《www.aljazeera.com》.
3. ↑ 가 나 “Generative AI: a game-changer society needs to be ready for”. 《World Economic Forum》.
4. ↑ “The A to Z of Artificial Intelligence”. 《Time》. 2023년 4월 13일.
5. ↑ Toews, Rob. “The Next Generation Of Large Language Models”. 《Forbes》.
6. ↑ https://www.forbes.com/sites/joemckendrick/2023/03/26/most-jobs-soon-to-be-influenced-by-artificial-intelligence-research-out-of-openai-and-university-of-pennsylvania-suggests/?sh=420f9c8f73c7
7. ↑ “News” (보도 자료).
8. ↑ Morrison, Ryan (2023년 3월 7일). “Salesforce launches EinsteinGPT built with OpenAI technology”. 《Tech Monitor》.
9. ↑ “The ChatGPT of Finance is Here, Bloomberg is Combining AI and Fintech”. 《Forbes》.
10. ↑ Hinton (et-al), Geoffrey (2012년 10월 15일). “Deep neural networks for acoustic modeling in speech recognition” (PDF). 《IEEE SIGNAL PROCESSING MAGAZINE》. Digital Object Identifier 10.1109/MSP.2012.2205597.
11. ↑ “A tutorial survey of architectures, algorithms, and applications for deep learning | APSIPA Transactions on Signal and Information Processing | Cambridge Core”. Cambridge.org. 2014년 1월 22일. doi:10.1017/atsip.2013.9. 2023년 5월 21일에 확인함.
12. ↑ Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Lukasz; Polosukhin, Illia (2017년 12월 5일). “Attention Is All You Need”. arXiv:1706.03762 – arXiv.org 경유.
13. ↑ Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (2019년 5월 24일). “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”. arXiv:1810.04805v2 – arXiv.org 경유.
14. ↑ Yang (et-al), Zhilin (2019). “XLNet” (PDF). 《Proceedings from NeurIPS 2019》.
15. ↑ Naik, Amit Raja (2021년 9월 23일). “Google Introduces New Architecture To Reduce Cost Of Transformers”. 《Analytics India Magazine》.
16. ↑ 가 나 다 Radford, Alec; Narasimhan, Karthik; Salimans, Tim; Sutskever, Ilya (2018년 6월 11일). “Improving Language Understanding by Generative Pre-Training” (PDF). OpenAI. 12쪽. 2021년 1월 26일에 원본 문서 (PDF)에서 보존된 문서. 2021년 1월 23일에 확인함.
17. ↑ Zhu, Yukun; Kiros, Ryan; Zemel, Rich; Salakhutdinov, Ruslan; Urtasun, Raquel; Torralba, Antonio; Fidler, Sanja (2015). 《Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books》. IEEE International Conference on Computer Vision (ICCV) 2015. 19–27쪽. arXiv:1506.06724. 2023년 2월 5일에 원본 문서에서 보존된 문서. 2023년 2월 7일에 확인함.
18. ↑ Brown, Tom B.; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; Kaplan, Jared; Dhariwal, Prafulla; Neelakantan, Arvind; Shyam, Pranav; Sastry, Girish; Askell, Amanda; Agarwal, Sandhini; Herbert-Voss, Ariel; Krueger, Gretchen; Henighan, Tom; Child, Rewon; Ramesh, Aditya; Ziegler, Daniel M.; Wu, Jeffrey; Winter, Clemens; Hesse, Christopher; Chen, Mark; Sigler, Eric; Litwin, Mateusz; Gray, Scott; Chess, Benjamin; Clark, Jack; Berner, Christopher; McCandlish, Sam; Radford, Alec; Sutskever, Ilya; Amodei, Dario (2020년 7월 22일). “Language Models are Few-Shot Learners”. arXiv:2005.14165v4 – arXiv.org 경유.
19. ↑ OpenAI (2023). “GPT-4 Technical Report” (PDF). 2023년 3월 14일에 원본 문서 (PDF)에서 보존된 문서. 2023년 3월 16일에 확인함.
20. ↑ Bommasani (et-al), Rishi (2022년 7월 12일). “On the Opportunities and Risks of Foundation Models” (PDF). 《arXiv》.
21. ↑ “Aligning language models to follow instructions”. 《openai.com》. 2023년 3월 23일에 원본 문서에서 보존된 문서. 2023년 3월 23일에 확인함.
22. ↑ Ouyang, Long; Wu, Jeff; Jiang, Xu; 외. (2022년 3월 4일). “Training language models to follow instructions with human feedback”. arXiv:2203.02155.
23. ↑ Ramnani, Meeta (2022년 1월 28일). “OpenAI dumps its own GPT-3 for something called InstructGPT, and for right reason”. 《Analytics India Magazine》.
24. ↑ “Stanford CRFM”. 《crfm.stanford.edu》.
25. ↑ “Free Dolly: Introducing the World's First Truly Open Instruction-Tuned LLM”. 《Databricks》. 2023년 4월 12일.
26. ↑ “Introducing ChatGPT”. 《openai.com》 (미국 영어). 2023년 3월 16일에 원본 문서에서 보존된 문서. 2023년 3월 16일에 확인함.
27. ↑ Wiggers, Kyle (2023년 5월 4일). “Microsoft doubles down on AI with new Bing features”.
28. ↑ “ChatGPT vs. Bing vs. Google Bard: Which AI Is the Most Helpful?”. 《CNET》.
29. ↑ “Auto-GPT, BabyAGI, and AgentGPT: How to use AI agents”. 《Mashable》. 2023년 4월 19일.
30. ↑ Marr, Bernard. “Auto-GPT May Be The Strong AI Tool That Surpasses ChatGPT”. 《Forbes》.
31. ↑ GPT-4.5가 인간을 이겼다…진짜 튜링 테스트 통과, 디지털 투데이, 2025.04.02, https://www.digitaltoday.co.kr/news/articleView.html?idxno=559761
32. ↑ GPT-4.5가 통과한 튜링 테스트가 뭐지?, AI 매터스, 2025년 04월 10일, https://aimatters.co.kr/news-report/feature-article/19094/
33. ↑ Large Language Models Pass the Turing Test, Cameron R. Jones, Benjamin K. Bergen, 31 Mar 2025, https://arxiv.org/abs/2503.23674

- v
- t
- e

- AI-완전
- 단어 가방 모형
- n-gram Bigram Trigram
- 전산언어학
- 자연어 이해
- 불용어
- 텍스트 처리

- Bigram
- Trigram

- 연어 추출
- Concept mining
- 공통참조해결
- Deep linguistic processing
- Distant reading
- 정보 추출
- 개체명 인식
- 온톨로지 학습
- 구문 분석
- 품사 태깅
- 의미역 결정
- 의미 유사도
- 감성 분석
- 용어 추출
- 텍스트 마이닝
- Textual entailment
- Truecasing
- 단어 중의성 해소
- Word-sense induction

- Compound-term processing
- 표제어 추출
- 낱말 분석
- Text chunking
- 어간 추출
- 문장 분할
- 단어 분절

- 다중 문서 요약
- 문장 추출
- 텍스트 단순화

- 컴퓨터 보조
- 예시 기반 번역
- 규칙 기반 번역
- 통계적
- 전이학습 기반 번역
- 신경망

- BERT
- 문서-단어 행렬
- 명시 의미 분석
- fastText
- GloVe
- 잠재 의미 분석
- 단어 임베딩
- Word2vec

- 말뭉치언어학
- Lexical resource
- Linguistic Linked Open Data
- 기계 가독형 사전
- 병렬말뭉치
- PropBank
- 시맨틱 네트워크
- Simple Knowledge Organization System
- 음성 코퍼스
- 말뭉치
- Thesaurus (information retrieval)
- Treebank
- 보편 의존

- BabelNet
- Bank of English
- 디비피디아
- FrameNet
- 구글 엔그램 뷰어
- UBY
- 워드넷

- 음성 인식
- 음성 분할
- 음성 합성
- 자연어 생성
- 광학 문자 인식

- 문서 분류
- 잠재 디리클레 할당
- 파친코 할당

- 작문 자동 채점
- Concordancer
- 문법 검사기
- 예측 문자
- 맞춤법 검사기
- 문법 예측

- 챗봇
- 인터랙티브 픽션
- 질의 응답
- 가상 비서
- 음성 사용자 인터페이스

- Natural Language Toolkit
- spaCy

- v
- t
- e

- 챗GPT
- DALL-E
- 깃허브 코파일럿
- 오픈AI 파이브
- 소라

- 오픈AI 코덱스
- GPT GPT-2 GPT-3 GPT-4

- GPT-2
- GPT-3
- GPT-4

- 샘 올트먼
- 미라 무라티

- 로런스 서머스

- 그렉 브로크만 (2017–2023)
- 리드 호프만 (2019–2023)
- 일론 머스크 (2015–2018)
- 일리야 수츠케버 (2017–2023)

- AI 던전
- Auto-GPT
- 딥 러닝
- 랭체인
- 마이크로소프트 365 코파일럿
- 마이크로소프트 빙

- 분류
- 공용