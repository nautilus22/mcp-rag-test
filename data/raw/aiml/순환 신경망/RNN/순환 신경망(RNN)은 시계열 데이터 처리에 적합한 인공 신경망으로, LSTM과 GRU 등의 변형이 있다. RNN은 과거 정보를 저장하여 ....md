---
title: 순환 신경망
type: 위키피디아 문서
format: markdown
---

# 순환 신경망

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

**순환 신경망**(Recurrent neural network, **RNN**)은 [인공 신경망](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D)의 한 종류로, 유닛간의 연결이 [순환](https://ko.wikipedia.org/wiki/%EC%88%9C%ED%99%98_(%EA%B7%B8%EB%9E%98%ED%94%84_%EC%9D%B4%EB%A1%A0))적 구조를 갖는 특징을 갖고 있다. 이러한 구조는 시변적 동적 특징을 모델링 할 수 있도록 신경망 내부에 상태를 저장할 수 있게 해주므로, [순방향 신경망](https://ko.wikipedia.org/wiki/%EC%88%9C%EB%B0%A9%ED%96%A5_%EC%8B%A0%EA%B2%BD%EB%A7%9D)과 달리 내부의 [메모리](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EB%A6%AC)를 이용해 [시퀀스](https://ko.wikipedia.org/wiki/%EC%8B%9C%ED%80%80%EC%8A%A4) 형태의 입력을 처리할 수 있다. 따라서 순환 인공 신경망은 [필기 인식](https://ko.wikipedia.org/wiki/%ED%95%84%EA%B8%B0_%EC%9D%B8%EC%8B%9D)이나 [음성 인식](https://ko.wikipedia.org/wiki/%EC%9D%8C%EC%84%B1_%EC%9D%B8%EC%8B%9D)과 같이 시변적 특징을 지니는 데이터를 처리하는데 적용할 수 있다.

순환 신경망이라는 이름은 입력받는 신호의 길이가 한정되지 않은 [동적](https://ko.wikipedia.org/wiki/%EB%8F%99%EC%97%AD%ED%95%99%EA%B3%84) 데이터를 처리한다는 점에서 붙여진 이름으로, [유한 임펄스](https://ko.wikipedia.org/w/index.php?title=%EC%9C%A0%ED%95%9C_%EC%9E%84%ED%8E%84%EC%8A%A4_%EC%9D%91%EB%8B%B5&action=edit&redlink=1) 구조와 [무한 임펄스](https://ko.wikipedia.org/w/index.php?title=%EB%AC%B4%ED%95%9C_%EC%9E%84%ED%8E%84%EC%8A%A4_%EC%9D%91%EB%8B%B5&action=edit&redlink=1) 구조를 모두 일컫는다. 유한 임펄스 순환 신경망은 [유향 비순환 그래프](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%96%A5_%EB%B9%84%EC%88%9C%ED%99%98_%EA%B7%B8%EB%9E%98%ED%94%84)이므로 적절하게 풀어서 재구성한다면 순방향 신경망으로도 표현할 수 있지만, 무한 임펄스 순환 신경망은 [유향 그래프](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%96%A5_%EA%B7%B8%EB%9E%98%ED%94%84)이므로 순방향 신경망으로 표현하는 것이 불가능하다.

순환 신경망은 추가적인 저장공간을 가질 수 있다. 이 저장공간이 그래프의 형태를 가짐으로써 시간 지연의 기능을 하거나 피드백 루프를 가질 수도 있다. 이와 같은 저장공간을 게이트된 상태(gated state) 또는 게이트된 메모리(gated memory)라고 하며, [LSTM](https://ko.wikipedia.org/wiki/LSTM)과 [게이트 순환 유닛](https://ko.wikipedia.org/wiki/%EA%B2%8C%EC%9D%B4%ED%8A%B8_%EC%88%9C%ED%99%98_%EC%9C%A0%EB%8B%9B)(GRU)이 이를 응용하는 대표적인 예시이다.

### 역사

RNN은 1986년 [데이비드 루멜하르트](https://ko.wikipedia.org/w/index.php?title=%EB%8D%B0%EC%9D%B4%EB%B9%84%EB%93%9C_%EB%9F%BC_%EB%A9%9C%ED%95%98%ED%8A%B8&action=edit&redlink=1)의 연구에 기반을 둔다. RNN의 특수한 예시인 홉필드 네트워크가 1982년 [존 홉필드](https://ko.wikipedia.org/wiki/%EC%A1%B4_%ED%99%89%ED%95%84%EB%93%9C)에 의해 발명되었고, 1993년에는 신경 기억 압축기가 "Very Deep Learning"를 구현하는데 성공했는데, 1000개 이상의 레이어로 구성된 정적 RNN이 사용되었다.

#### LSTM

1997년 [혹스라이터](https://ko.wikipedia.org/w/index.php?title=Sepp_Hochreiter&action=edit&redlink=1)와 [슈미트후버](https://ko.wikipedia.org/w/index.php?title=%EC%9C%84%EB%A5%B4%EA%B2%90_%EC%8A%88%EB%AF%B8%ED%8A%B8_%ED%9B%84%EB%B2%84&action=edit&redlink=1)에 의해 발명된 [LSTM](https://ko.wikipedia.org/wiki/LSTM)은 네트워크는 여러 응용분야에서 독보적인 정확성을 보여주었다.

2007년을 전후로, LSTM은 [음성 인식](https://ko.wikipedia.org/wiki/%EC%9D%8C%EC%84%B1_%EC%9D%B8%EC%8B%9D) 분야에서 기존의 전통적인 모델들을 아득히 능가하는 성능을 보여주었다. 2009년에는 CTC(Connectionist temporal classification) 기술로 훈련시킨 LSTM이 처음으로 [필기체 인식](https://ko.wikipedia.org/wiki/%ED%95%84%EA%B8%B0_%EC%9D%B8%EC%8B%9D) 시합에서 승리를 거둠으로써, 패턴 인식 분야에 독보적인 기능을 가지고 있음이 증명되었다. 2014년에는 중국의 검색엔진인 [바이두](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%EB%91%90)가 기존의 음성 인식 알고리즘은 전혀 사용하지 않고 오직 CTC로 훈련된 RNN만으로 [Switchboard Hub5'00 speech recognition dataset](https://catalog.ldc.upenn.edu/LDC2002S09) 벤치마크를 갱신했다.

LSTM은 또한 큰 단어에 대한 음성 인식과 [음성 합성](https://ko.wikipedia.org/wiki/%EC%9D%8C%EC%84%B1_%ED%95%A9%EC%84%B1) 분야에서도 발전을 이루어 현재 [구글 안드로이드](https://ko.wikipedia.org/wiki/%EA%B5%AC%EA%B8%80_%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C)에서 응용되고있다. 2015년에는 구글의 음성 인식 능력이 CTC 기반 LSTM을 통해 49%가량 향상되었다.

또한 [기계 번역](https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%EB%B2%88%EC%97%AD), [언어 모델링](https://ko.wikipedia.org/wiki/%EC%96%B8%EC%96%B4_%EB%AA%A8%EB%8D%B8), 다국어 언어 처리 분야에서의 기록도 우수한 능력으로 연달아 갱신했다. [합성곱 신경망](https://ko.wikipedia.org/wiki/%ED%95%A9%EC%84%B1%EA%B3%B1_%EC%8B%A0%EA%B2%BD%EB%A7%9D)과 함께 응용되어 [자동 이미지 캡셔닝](https://ko.wikipedia.org/w/index.php?title=%EC%9E%90%EB%8F%99_%EC%9D%B4%EB%AF%B8%EC%A7%80_%EC%BA%A1%EC%85%94%EB%8B%9D&action=edit&redlink=1) 분야에서도 커다란 향상을 일으켰다. LSTM을 돌리는데 필요한 막대한 계산량에 따른 하드웨어의 부담을 줄이기 위해 하드웨어 가속기를 사용해 LSTM을 가속하고자 하는 연구도 꾸준히 진행되고 있다.

### 구조

#### 완전순환(Fully recurrent)

RNN은 [뉴런과 유사한](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5_%EB%89%B4%EB%9F%B0) 노드들이 이룬 레이어가 연속되어있는 구조를 가진다. 각각의 노드들은 다음 단계의 모든 레이어들과 [단방향 그래프](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%96%A5_%EA%B7%B8%EB%9E%98%ED%94%84)를 이루며, 시간에 따라 달라지는 실숫값의 활성화(activation)값을 가진다. 또한 각 노드들 간 연결관계는 실숫값의 [가중치](https://ko.wikipedia.org/w/index.php?title=%EA%B0%80%EC%A4%91%EC%B9%98&action=edit&redlink=1)를 가지며 이 값은 끊임없이 바뀐다. 노드의 종류로는 신경망 외부로부터 값을 입력받는 입력 노드, 결괏값을 산출하는 출력 노드, 입력 노드에서 출력 노드 사이에 존재하는 은닉 노드가 있다.

이산 시간 데이터로 [지도 학습](https://ko.wikipedia.org/wiki/%EC%A7%80%EB%8F%84_%ED%95%99%EC%8A%B5)을 하는 경우, 단위시간 한 번에 실수 벡터 하나가 입력 노드로 들어온다. 또한 매 순간 입력 노드를 제외한 모든 노드들은, 각자 연결된 노드들로부터 활성화값을 각 연결의 가중치와 함께 가중합으로 받아, 비선형 함수를 통해 활성화값을 계산한 뒤 저장한다. 지도 학습을 위해 주어진 데이터는 특정 순간마다 출력 노드 값이 이루어야 하는 값(target)을 알려준다. 매 순간마다 신경망이 생성한 출력값과, 원래 이루었어야 하는 값 사이의 편차의 합으로 오차를 정의한다. 이 오차를 줄이는 방향으로 신경망의 학습이 이루어진다. 일례로 음성 인식을 통해 발음된 숫자를 알아맞추는 프로그램을 생각해보자. 이 경우 최종 출력값은 숫자를 분류하기 위한 레이블이 될 것이다.

[강화 학습](https://ko.wikipedia.org/wiki/%EA%B0%95%ED%99%94_%ED%95%99%EC%8A%B5)의 경우, 아무도 출력 값이 어떠해야한다는 정보를 가르쳐주지 않는다. 대신 RNN의 성능을 평가하기 위한 [적합성 함수](https://ko.wikipedia.org/w/index.php?title=%EC%A0%81%ED%95%A9%EC%84%B1_%ED%95%A8%EC%88%98&action=edit&redlink=1)(영어:[fitness function](https://en.wikipedia.org/wiki/fitness_function))나 보상 함수가 출력값을 받아들인 뒤, 액츄에이터를 통해 환경에 영향을 줌으로써 입력값을 변화시킨다. 점수가 있는 게임을 플레이하는 인공지능을 만들 때 이런 기술을 사용할 수 있다.

#### 단순 순환망

엘만 신경망과 조르단 신경망을 단순 순환망(Simple recurrent network, SRN)이라 부른다.

엘만 신경망은 세 개의 레이어와 문맥 유닛으로 이루어져 있으며, 문맥 유닛들은 1로 고정된 가중치와 함께 은닉 레이어와 연결되어 있다. 학습이 이루어질 때마다 입력값이 순방향으로 되먹임되고, 은닉 레이어가 전 단계에 가지고 있던 값이 문맥 유닛에 저장된다. 따라서 신경망은 과거의 상태를 저장할 수 있게됨으로써 일반적인 [다중계층 퍼셉트론](https://ko.wikipedia.org/w/index.php?title=%EB%8B%A4%EC%A4%91%EA%B3%84%EC%B8%B5_%ED%8D%BC%EC%85%89%ED%8A%B8%EB%A1%A0&action=edit&redlink=1)보다 우수한 예지력을 가지게 되는 것이다.

조르단 신경망은 엘만 신경망과 비슷하나, 문맥 유닛이 은닉 레이어가 아닌 출력 레이어로부터 값을 받는다는 차이점이 있다. 이 경우 문맥 유닛은 상태 레이어라고 불리며, 그 내부에서도 순환망을 가진다.

위 식에서 기호들은 각각 다음을 의미한다.

- $\displaystyle x_{t}}$: 입력 벡터
- $\displaystyle h_{t}}$: 은닉 레이어 벡터
- $\displaystyle y_{t}}$: 출력 벡터
- $\displaystyle W}$, $\displaystyle U}$, $\displaystyle b}$: 매개변수 행렬과 벡터
- $\displaystyle \sigma _{h}}$, $\displaystyle \sigma _{y}}$: 활성화 함수

#### LSTM

LSTM(long short-term memory, 장단기 메모리)는 [기울기 소실 문제](https://ko.wikipedia.org/wiki/%EA%B8%B0%EC%9A%B8%EA%B8%B0_%EC%86%8C%EC%8B%A4_%EB%AC%B8%EC%A0%9C)를 해결하기 위해 고안된 [딥 러닝](https://ko.wikipedia.org/wiki/%EB%94%A5_%EB%9F%AC%EB%8B%9D) 시스템이다. LSTM은 망각 게이트(forget gate)라 부르는 게이트를 추가적으로 가진다. 이 게이트를 통해 역전파시 기울기값이 급격하게 사라지거나 증가하는 문제를 방지할 수 있다. 이로써 기존의 RNN은 먼 과거의 일로부터 학습하는 것이 산술적으로 거의 불가능했지만, LSTM은 수백만 단위 시간 전의 사건으로부터도 학습할 수 있음으로서 고주파 신호뿐 아니라 저주파 신호까지도 다룰 수 있게 되었고, 이는 곧 성능의 비약적 발전을 가져왔다. 이로써 LSTM과 유사한 구조를 가진 신경망들도 많이 발표되고 있다.

LSTM을 쌓은 뒤 [CTC](https://ko.wikipedia.org/w/index.php?title=CTC_(%EB%94%A5_%EB%9F%AC%EB%8B%9D)&action=edit&redlink=1)(영어:[Connectionist temporal classification](https://en.wikipedia.org/wiki/Connectionist_temporal_classification))로 이 신경망을 학습시키는 방식으로 실제 연구분야에 많이 사용되고 있다. 특히 CTC는 정렬과 인식에서 좋은 결과를 가져다주고 있다. 또한 기존의 [은닉 마르코프 모형](https://ko.wikipedia.org/wiki/%EC%9D%80%EB%8B%89_%EB%A7%88%EB%A5%B4%EC%BD%94%ED%94%84_%EB%AA%A8%ED%98%95)(HMM)으로는 불가능했던 문맥의존언어 학습이 가능하다는 것이 밝혀졌다.

#### GRU

GRU(Gated recurrent units, [게이트 순환 유닛](https://ko.wikipedia.org/wiki/%EA%B2%8C%EC%9D%B4%ED%8A%B8_%EC%88%9C%ED%99%98_%EC%9C%A0%EB%8B%9B))은 2014년에 처음으로 발명된 구조다. 처음 발표된 형태로 적용되기도 하나, 간단하게 변용되는 경우도 많다. 출력 게이트가 존재하지 않으므로, LSTM에 비해 더 적은 수의 매개변수를 가짐에도 불구하고 [다성음악](https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%84%B1%EC%9D%8C%EC%95%85) 학습이나 음성 인식 분야에서 LSTM과 유사한 성능을 가진다.

#### 양방향

양방향(Bi-directional) 순환 신경망은 길이가 정해진 데이터 순열을 통해 어떤 값이 들어오기 전과 후의 정보를 모두 학습하는 방식의 알고리즘이다. 이를 위해 순열을 왼쪽에서 오른쪽으로 읽을 RNN 하나와, 오른쪽에서 왼쪽으로 읽을 RNN 하나를 필요로 한다. 이 둘의 출력값을 조합한 뒤 지도된 결과와 비교하여 학습하는 것이다. LSTM과 병용할 때 특히 좋은 성능을 낸다는 사실이 증명되었다.

### 응용 분야

순환 신경망의은 다음과 같은 분야에서 응용될 수 있다.

- 기계 번역
- 로봇 제어
- 시계열 예측
- 음성 인식
- 음성 합성
- 시계열 오류 검출
- 리듬 학습
- 작곡
- 문법 학습
- 필기 인식
- 인간 행동 인식
- 단백질간 상동성 발견
- 단백질의 세포내 배치 분석
- 비즈니스 프로세스 관리 및 예측

### 각주

1. ↑ Dupond, Samuel (2019). “A thorough review on the current advance of neural network structures.”. 《Annual Reviews in Control》 14: 200–230.
2. ↑ “State-of-the-art in artificial neural network applications: A survey”. 《Heliyon》 (영어) 4 (11): e00938. 2018년 11월 1일. doi:10.1016/j.heliyon.2018.e00938. ISSN 2405-8440.
3. ↑ “Time series forecasting using artificial neural networks methodologies: A systematic review”. 《Future Computing and Informatics Journal》 (영어) 3 (2): 334–340. 2018년 12월 1일. doi:10.1016/j.fcij.2018.10.003. ISSN 2314-7288.
4. ↑ Graves, A.; Liwicki, M.; Fernandez, S.; Bertolami, R.; Bunke, H.; Schmidhuber, J. (2009). “A Novel Connectionist System for Improved Unconstrained Handwriting Recognition” (PDF). 《IEEE Transactions on Pattern Analysis and Machine Intelligence》 31 (5): 855–868. doi:10.1109/tpami.2008.137. PMID 19299860.
5. ↑ Sak, Hasim; Senior, Andrew; Beaufays, Francoise (2014). “Long Short-Term Memory recurrent neural network architectures for large scale acoustic modeling” (PDF).
6. ↑ 봇이 이 인용을 자동으로 완성합니다. 대기열로 바로 이동하기 arXiv:.
7. ↑ Miljanovic, Milos (Feb-Mar 2012). “Comparative analysis of Recurrent and Finite Impulse Response Neural Networks in Time Series Prediction” (PDF). 《Indian Journal of Computer and Engineering》 3 (1). 다음 날짜 값 확인 필요: |date= (도움말)
8. ↑ Williams, Ronald J.; Hinton, Geoffrey E.; Rumelhart, David E. (October 1986). “Learning representations by back-propagating errors”. 《Nature》 323 (6088): 533–536. doi:10.1038/323533a0. ISSN 1476-4687.
9. ↑ Schmidhuber, Jürgen (1993). 《Habilitation thesis: System modeling and optimization》 (PDF). [깨진 링크(과거 내용 찾기)] Page 150 ff demonstrates credit assignment across the equivalent of 1,200 layers in an unfolded RNN.
10. ↑ Hochreiter, Sepp; Schmidhuber, Jürgen (1997년 11월 1일). “Long Short-Term Memory”. 《Neural Computation》 9 (8): 1735–1780. doi:10.1162/neco.1997.9.8.1735.
11. ↑ Fernández, Santiago; Graves, Alex; Schmidhuber, Jürgen (2007). 《An Application of Recurrent Neural Networks to Discriminative Keyword Spotting》. 《Proceedings of the 17th International Conference on Artificial Neural Networks》. ICANN'07 (Berlin, Heidelberg: Springer-Verlag). 220–229쪽. ISBN 978-3-540-74693-5.
12. ↑ 가 나 Schmidhuber, Jürgen (January 2015). “Deep Learning in Neural Networks: An Overview”. 《Neural Networks》 61: 85–117. arXiv:1404.7828. doi:10.1016/j.neunet.2014.09.003. PMID 25462637. S2CID 11715509.
13. ↑ Graves, Alex; Schmidhuber, Jürgen (2009). Bengio, Yoshua; Schuurmans, Dale; Lafferty, John; Williams, Chris editor-K. I.; Culotta, Aron, 편집. “Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks”. Neural Information Processing Systems (NIPS) Foundation: 545–552.
14. ↑ Hannun, Awni; Case, Carl; Casper, Jared; Catanzaro, Bryan; Diamos, Greg; Elsen, Erich; Prenger, Ryan; Satheesh, Sanjeev; Sengupta, Shubho (2014년 12월 17일). “Deep Speech: Scaling up end-to-end speech recognition”. arXiv:1412.5567 [cs.CL]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
15. ↑ Sak, Haşim; Senior, Andrew; Beaufays, Françoise (2014). “Long Short-Term Memory recurrent neural network architectures for large scale acoustic modeling” (PDF). 2019년 9월 22일에 원본 문서 (PDF)에서 보존된 문서. 2020년 10월 8일에 확인함.
16. ↑ Li, Xiangang; Wu, Xihong (2014년 10월 15일). “Constructing Long Short-Term Memory based Deep Recurrent Neural Networks for Large Vocabulary Speech Recognition”. arXiv:1410.4281 [cs.CL]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
17. ↑ Fan, Bo; Wang, Lijuan; Soong, Frank K.; Xie, Lei (2015) "Photo-Real Talking Head with Deep Bidirectional LSTM", in Proceedings of ICASSP 2015
18. ↑ Zen, Heiga; Sak, Haşim (2015). “Unidirectional Long Short-Term Memory Recurrent Neural Network with Recurrent Output Layer for Low-Latency Speech Synthesis” (PDF). 《Google.com》. ICASSP. 4470–4474쪽.
19. ↑ Sak, Haşim; Senior, Andrew; Rao, Kanishka; Beaufays, Françoise; Schalkwyk, Johan (September 2015). “Google voice search: faster and more accurate”.
20. ↑ Sutskever, Ilya; Vinyals, Oriol; Le, Quoc V. (2014). “Sequence to Sequence Learning with Neural Networks” (PDF). 《Electronic Proceedings of the Neural Information Processing Systems Conference》 27: 5346. arXiv:1409.3215. Bibcode:2014arXiv1409.3215S.
21. ↑ Jozefowicz, Rafal; Vinyals, Oriol; Schuster, Mike; Shazeer, Noam; Wu, Yonghui (2016년 2월 7일). “Exploring the Limits of Language Modeling”. arXiv:1602.02410 [cs.CL]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
22. ↑ Gillick, Dan; Brunk, Cliff; Vinyals, Oriol; Subramanya, Amarnag (2015년 11월 30일). “Multilingual Language Processing From Bytes”. arXiv:1512.00103 [cs.CL]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
23. ↑ Vinyals, Oriol; Toshev, Alexander; Bengio, Samy; Erhan, Dumitru (2014년 11월 17일). “Show and Tell: A Neural Image Caption Generator”. arXiv:1411.4555 [cs.CV]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
24. ↑ "A Survey on Hardware Accelerators and Optimization Techniques for RNNs", JSA, 2020 PDF
25. ↑ 가 나 Cruse, Holk; Neural Networks as Cybernetic Systems, 2nd and revised edition
26. ↑ Elman, Jeffrey L. (1990). “Finding Structure in Time”. 《Cognitive Science》 14 (2): 179–211. doi:10.1016/0364-0213(90)90002-E.
27. ↑ Jordan, Michael I. (1997년 1월 1일). 〈Serial Order: A Parallel Distributed Processing Approach〉. 《Neural-Network Models of Cognition - Biobehavioral Foundations》. 《Advances in Psychology》. Neural-Network Models of Cognition 121. 471–495쪽. doi:10.1016/s0166-4115(97)80111-2. ISBN 9780444819314.
28. ↑ Gers, Felix A.; Schraudolph, Nicol N.; Schmidhuber, Jürgen (2002). “Learning Precise Timing with LSTM Recurrent Networks” (PDF). 《Journal of Machine Learning Research》 3: 115–143. 2017년 6월 13일에 확인함.
29. ↑ Hochreiter, Sepp (1991), Untersuchungen zu dynamischen neuronalen Netzen, Diploma thesis, Institut f. Informatik, Technische Univ. Munich, Advisor Jürgen Schmidhuber
30. ↑ Schmidhuber, Jürgen (January 2015). “Deep Learning in Neural Networks: An Overview”. 《Neural Networks》 61: 85–117. arXiv:1404.7828. doi:10.1016/j.neunet.2014.09.003. PMID 25462637. S2CID 11715509.
31. ↑ Bayer, Justin; Wierstra, Daan; Togelius, Julian; Schmidhuber, Jürgen (2009년 9월 14일). 《Evolving Memory Cell Structures for Sequence Learning》 (PDF). 《Artificial Neural Networks – ICANN 2009》. Lecture Notes in Computer Science 5769 (Berlin, Heidelberg: Springer). 755–764쪽. doi:10.1007/978-3-642-04277-5_76. ISBN 978-3-642-04276-8.
32. ↑ Fernández, Santiago; Graves, Alex; Schmidhuber, Jürgen (2007). “Sequence labelling in structured domains with hierarchical recurrent neural networks”. 《Proc. 20th International Joint Conference on Artificial In℡ligence, Ijcai 2007》: 774–779. CiteSeerX 10.1.1.79.1887.
33. ↑ Graves, Alex; Fernández, Santiago; Gomez, Faustino J. (2006). “Connectionist temporal classification: Labelling unsegmented sequence data with recurrent neural networks”. 《Proceedings of the International Conference on Machine Learning》: 369–376. CiteSeerX 10.1.1.75.6306.
34. ↑ Gers, Felix A.; Schmidhuber, Jürgen (November 2001). “LSTM recurrent networks learn simple context-free and context-sensitive languages”. 《IEEE Transactions on Neural Networks》 12 (6): 1333–1340. doi:10.1109/72.963769. ISSN 1045-9227. PMID 18249962. S2CID 10192330.
35. ↑ Heck, Joel; Salem, Fathi M. (2017년 1월 12일). “Simplified Minimal Gated Unit Variations for Recurrent Neural Networks”. arXiv:1701.03452 [cs.NE]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
36. ↑ Dey, Rahul; Salem, Fathi M. (2017년 1월 20일). “Gate-Variants of Gated Recurrent Unit (GRU) Neural Networks”. arXiv:1701.05923 [cs.NE]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
37. ↑ Britz, Denny (2015년 10월 27일). “Recurrent Neural Network Tutorial, Part 4 – Implementing a GRU/LSTM RNN with Python and Theano – WildML”. 《Wildml.com》. 2021년 11월 10일에 원본 문서에서 보존된 문서. 2016년 5월 18일에 확인함.
38. ↑ Chung, Junyoung; Gulcehre, Caglar; Cho, KyungHyun; Bengio, Yoshua (2014). “Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling”. arXiv:1412.3555 [cs.NE]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
39. ↑ Graves, Alex; Schmidhuber, Jürgen (2005년 7월 1일). “Framewise phoneme classification with bidirectional LSTM and other neural network architectures”. 《Neural Networks》. IJCNN 2005 18 (5): 602–610. CiteSeerX 10.1.1.331.5800. doi:10.1016/j.neunet.2005.06.042. PMID 16112549.
40. ↑ Thireou, Trias; Reczko, Martin (July 2007). “Bidirectional Long Short-Term Memory Networks for Predicting the Subcellular Localization of Eukaryotic Proteins”. 《IEEE/ACM Transactions on Computational Biology and Bioinformatics》 4 (3): 441–446. doi:10.1109/tcbb.2007.1015. PMID 17666763. S2CID 11787259.
41. ↑ Sutskever, Ilya; Vinyals, Oriol; Le, Quoc V. (2014). “Sequence to Sequence Learning with Neural Networks” (PDF). 《Electronic Proceedings of the Neural Information Processing Systems Conference》 27: 5346. arXiv:1409.3215. Bibcode:2014arXiv1409.3215S.
42. ↑ Mayer, Hermann; Gomez, Faustino J.; Wierstra, Daan; Nagy, Istvan; Knoll, Alois; Schmidhuber, Jürgen (October 2006). 《A System for Robotic Heart Surgery that Learns to Tie Knots Using Recurrent Neural Networks》. 《2006 IEEE/RSJ International Conference on Intelligent Robots and Systems》. 543–548쪽. CiteSeerX 10.1.1.218.3399. doi:10.1109/IROS.2006.282190. ISBN 978-1-4244-0258-8. S2CID 12284900.
43. ↑ Wierstra, Daan; Schmidhuber, Jürgen; Gomez, Faustino J. (2005). “Evolino: Hybrid Neuroevolution/Optimal Linear Search for Sequence Learning”. 《Proceedings of the 19th International Joint Conference on Artificial Intelligence (IJCAI), Edinburgh》: 853–858.
44. ↑ Petneházi, Gábor (2019년 1월 1일). “Recurrent neural networks for time series forecasting”. arXiv:1901.00069 [cs.LG]. 더 이상 지원되지 않는 변수를 사용함 (도움말)
45. ↑ Hewamalage, Hansika; Bergmeir, Christoph; Bandara, Kasun (2020). “Recurrent Neural Networks for Time Series Forecasting: Current Status and Future Directions”. 《International Journal of Forecasting》. arXiv:1909.00590. doi:10.1016/j.ijforecast.2020.06.008. S2CID 202540863.
46. ↑ Graves, Alex; Schmidhuber, Jürgen (2005). “Framewise phoneme classification with bidirectional LSTM and other neural network architectures”. 《Neural Networks》 18 (5–6): 602–610. CiteSeerX 10.1.1.331.5800. doi:10.1016/j.neunet.2005.06.042. PMID 16112549.
47. ↑ Fernández, Santiago; Graves, Alex; Schmidhuber, Jürgen (2007). 《An Application of Recurrent Neural Networks to Discriminative Keyword Spotting》. 《Proceedings of the 17th International Conference on Artificial Neural Networks》. ICANN'07 (Berlin, Heidelberg: Springer-Verlag). 220–229쪽. ISBN 978-3540746935.
48. ↑ Graves, Alex; Mohamed, Abdel-rahman; Hinton, Geoffrey E. (2013). “Speech Recognition with Deep Recurrent Neural Networks”. 《Acoustics, Speech and Signal Processing (ICASSP), 2013 IEEE International Conference on》: 6645–6649. arXiv:1303.5778. Bibcode:2013arXiv1303.5778G. doi:10.1109/ICASSP.2013.6638947. ISBN 978-1-4799-0356-6. S2CID 206741496.
49. ↑ Chang, Edward F.; Chartier, Josh; Anumanchipalli, Gopala K. (2019년 4월 24일). “Speech synthesis from neural decoding of spoken sentences”. 《Nature》 (영어) 568 (7753): 493–498. Bibcode:2019Natur.568..493A. doi:10.1038/s41586-019-1119-1. ISSN 1476-4687. PMID 31019317. S2CID 129946122.
50. ↑ Malhotra, Pankaj; Vig, Lovekesh; Shroff, Gautam; Agarwal, Puneet (April 2015). “Long Short Term Memory Networks for Anomaly Detection in Time Series” (PDF). 《European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning — ESANN 2015》. 2020년 10월 30일에 원본 문서 (PDF)에서 보존된 문서. 2020년 10월 8일에 확인함.
51. ↑ Gers, Felix A.; Schraudolph, Nicol N.; Schmidhuber, Jürgen (2002). “Learning precise timing with LSTM recurrent networks” (PDF). 《Journal of Machine Learning Research》 3: 115–143.
52. ↑ Eck, Douglas; Schmidhuber, Jürgen (2002년 8월 28일). 《Learning the Long-Term Structure of the Blues》. 《Artificial Neural Networks — ICANN 2002》. Lecture Notes in Computer Science 2415 (Berlin, Heidelberg: Springer). 284–289쪽. CiteSeerX 10.1.1.116.3620. doi:10.1007/3-540-46084-5_47. ISBN 978-3540460848.
53. ↑ Schmidhuber, Jürgen; Gers, Felix A.; Eck, Douglas (2002). “Learning nonregular languages: A comparison of simple recurrent networks and LSTM”. 《Neural Computation》 14 (9): 2039–2041. CiteSeerX 10.1.1.11.7369. doi:10.1162/089976602320263980. PMID 12184841. S2CID 30459046.
54. ↑ Gers, Felix A.; Schmidhuber, Jürgen (2001). “LSTM Recurrent Networks Learn Simple Context Free and Context Sensitive Languages” (PDF). 《IEEE Transactions on Neural Networks》 12 (6): 1333–1340. doi:10.1109/72.963769. PMID 18249962. 2020년 7월 10일에 원본 문서 (PDF)에서 보존된 문서. 2020년 10월 8일에 확인함.
55. ↑ Pérez-Ortiz, Juan Antonio; Gers, Felix A.; Eck, Douglas; Schmidhuber, Jürgen (2003). “Kalman filters improve LSTM network performance in problems unsolvable by traditional recurrent nets”. 《Neural Networks》 16 (2): 241–250. CiteSeerX 10.1.1.381.1992. doi:10.1016/s0893-6080(02)00219-8. PMID 12628609.
56. ↑ Graves, Alex; Schmidhuber, Jürgen (2009). “Offline Handwriting Recognition with Multidimensional Recurrent Neural Networks”. 《Advances in Neural Information Processing Systems 22, NIPS'22》 (Vancouver (BC): MIT Press): 545–552.
57. ↑ Graves, Alex; Fernández, Santiago; Liwicki, Marcus; Bunke, Horst; Schmidhuber, Jürgen (2007). 《Unconstrained Online Handwriting Recognition with Recurrent Neural Networks》. 《Proceedings of the 20th International Conference on Neural Information Processing Systems》. NIPS'07 (Curran Associates Inc.). 577–584쪽. ISBN 9781605603520.
58. ↑ Baccouche, Moez; Mamalet, Franck; Wolf, Christian; Garcia, Christophe; Baskurt, Atilla (2011). Salah, Albert Ali; Lepri, Bruno, 편집. “Sequential Deep Learning for Human Action Recognition”. 《2nd International Workshop on Human Behavior Understanding (HBU)》. Lecture Notes in Computer Science (Amsterdam, Netherlands: Springer) 7065: 29–39. doi:10.1007/978-3-642-25446-8_4. ISBN 978-3-642-25445-1.
59. ↑ Hochreiter, Sepp; Heusel, Martin; Obermayer, Klaus (2007). “Fast model-based protein homology detection without alignment”. 《Bioinformatics》 23 (14): 1728–1736. doi:10.1093/bioinformatics/btm247. PMID 17488755.
60. ↑ Thireou, Trias; Reczko, Martin (July 2007). “Bidirectional Long Short-Term Memory Networks for Predicting the Subcellular Localization of Eukaryotic Proteins”. 《IEEE/ACM Transactions on Computational Biology and Bioinformatics》 4 (3): 441–446. doi:10.1109/tcbb.2007.1015. PMID 17666763. S2CID 11787259.
61. ↑ Tax, Niek; Verenich, Ilya; La Rosa, Marcello; Dumas, Marlon (2017). 《Predictive Business Process Monitoring with LSTM neural networks》. 《Proceedings of the International Conference on Advanced Information Systems Engineering (CAiSE)》. Lecture Notes in Computer Science. 10253. 477–492쪽. arXiv:1612.02130. doi:10.1007/978-3-319-59536-8_30. ISBN 978-3-319-59535-1. S2CID 2192354.

### 더 읽어보기

- Mandic, Danilo P. & Chambers, Jonathon A. (2001). 《Recurrent Neural Networks for Prediction: Learning Algorithms, Architectures and Stability》. Wiley. ISBN 978-0-471-49517-8.

### 외부 링크

- Seq2SeqSharp LSTM/BiLSTM/Transformer recurrent neural networks framework running on CPUs and GPUs for sequence-to-sequence tasks (C#, .NET)
- RNNSharp CRFs based on recurrent neural networks (C#, .NET)
- Recurrent Neural Networks with over 60 RNN papers by Jürgen Schmidhuber's group at Dalle Molle Institute for Artificial Intelligence Research
- Elman Neural Network implementation for WEKA
- Recurrent Neural Nets & LSTMs in Java 보관됨 2018-07-21 - 웨이백 머신
- an alternative try for complete RNN / Reward driven 보관됨 2018-03-24 - 웨이백 머신

- 독일