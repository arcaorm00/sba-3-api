교과서 12장

ann, dnn

nn = (bool함수 + 활성화함수 + 계단함수), (), ()
cost function
ann / anns = dnn / dnn + col = cnn


프레임워크 vs 라이브러리

프레임워크: 틀. 정해진 틀에 우리가 맞춘다. (ex. Flask)
라이브러리: 도구. 도구를 가져다가 우리가 만든다. (ex. tensorflow)
==> 스프링의 경우 use라이브러리(디펜던시)

function y = WX + b
+ perceptron 활성화함수, 계단함수
활성화함수 (y = f(y = WX + b)) => 0 / 1 => perceptron
adalin 0.0 ~ 1.0

tensorflow도 결국 라이브러리이다. numpy나 pandas처럼. 너무 거대하게 생각할 필요가 없다.
use 텐서플로
work (in Flask (context)) in anaconda

텐서플로는 라이브러리
플라스크는 프레임워크
케라스는 API

교과서 13장

텐서플로: CPU / GPU(CUDA)
텐서플로는 알고리즘을 구현하고 실행하는 인터페이스를 가지고 있다.(p.460)

저수준 API: 자유도가 높다.
고수준 API: 자유도가 낮다. => 개발자가 커스터마이징할 요소가 적다.

노드: 0개 이상의 입력이나 출력을 가지는 연산 => 함수 (그래프 (=matrix) 연산)
세션에 넣어서 실행 --> '즉시 실행 모드'(세션을 히든) 추가

텐서는 스칼라, 벡터, 매트릭스 등이 일반화된 것.
스칼라: 랭크 0인 텐서
벡터: 랭크 1인 텐서
매트릭스: 랭크 2인 텐서
큐빅: 랭크 3인 텐서
랭크 4 이상인 텐서는 그릴 수 없고 수학적으로만 존재

https://ko.wikipedia.org/wiki/%ED%85%90%EC%84%9C
선형대수학에서, 다중선형사상(multilinear map)또는 텐서(tensor)는 
선형 관계를 나타내는 다중선형대수학의 대상이다.
19세기에 카를 프리드리히 가우스가 곡면에 대한 미분 기하학을 만들면서 도입하였다.
텐서는 기저(basis: n vector)를 선택하여 다차원 배열로 나타낼 수 있으며,
기저를 바꾸는 변환 법칙이 존재한다.

랭크가 곧 위 문장에서의 기저. 독립적 vector의 카운팅이자 variable한 차원의 단위 
t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ==> 랭크 2
https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/resources/dims_types.html

a = 0
b = 0.0
c = '0'

Variable, Const, placeholder
placeholder: 저수준 API 개발시 사용, 입력 데이터와 하이퍼파라미터 튜닝을 하는 곳
Weight(가중치) dimension 2

dnn = bool함수 + 활성화함수 + 손실함수 + 옵티마이저

손실함수를 안다는 것의 의미 => 에러를 알고 있다. => 값을 안다. 즉, 역전파.

평균 제곱 오차 MSE

self.w = tf.Variable(tf.zeros(shape=(1))) ==> 값이 모두 0인 vector
self.b = tf.Variable(tf.zeros(shape=(1))) ==> 값이 모두 0인 vector