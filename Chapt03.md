nn: neural network (=neurons)

neuron vs. neural network
단수 vs. 복수

json: {} 단수, [] 복수
java의 경우: member(객체), List<Member>(컬렉션) (컬렉션도 객체)

scalar vs. vector
단수 vs. 복수
변수 / 상수

int a = f({3, 4, 5})

y = f(x):   function
f(x):       consumer => setter
y = f():    supplier => getter
bool=f(x):  predicate
f():        runnable(x)

function + prop = object + object = collection

prop + prop = database

nue + ron: 이진 출력 ==> Y/N, 0/1 ==> bool 함수
percept(인지하다) + ron(뉴런): 인식하는 뉴런 ==> 확률 (가중치) ==> (bool 함수) + 계단 함수
adalin: (bool 함수 + 계단 함수) + 활성화 함수
우리가 만드는 함수들은 이 adalin 보다도 확장되기에 기본적으로 bool 함수 + 계단 함수 + 활성화 함수를 포함한다.

function + function = algorithm + algorithm = model + model = library

model이 dynamic의 개념이라면 machine은 static의 개념

neuron
perceptron 활성화함수 O, 계단함수
NN      활성화함수 O, 시그모이드, 이산 정수
    AI 겨울
    NN 단위 단수형 -> 복수형 (DNN) layer가 1개
    DNN     (deep) NN을 layer라고 부른다.
            {algo + nn + dframe + function(main)} ==> model
    CNN     활성화함수 O, ReLU, 연속 실수값
    RNN     
    lstm
    gan

하이퍼 파라미터: 은닉층에서 층으로 계속 전달 가능
단순 파라미터: 값 1회 전달 (입력층 -> 출력층)