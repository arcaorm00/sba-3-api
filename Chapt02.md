분류 알고리즘
    퍼셉트론 (항상 이진분류)
    아달린 (퍼셉트론의 향상된 버전)
        - 연속함수이며, 비용함수(cost function)를 정의하고 최소화
        - 퍼셉트론에서 활성화 함수가 추가된 것이 아달린이다.

1943 MCP
1957 Perceptron
1969 MLP 다층 퍼셉트론
1974 Backpropagation 역전파

함수: input T, output T State

Cost Function (비용함수)
Activation Function (활성화함수)
    - 선형 활성화
    - 비선형 활성화
Identity Function (항등함수)
Object Function (목적함수): 
    - 최적화 object function = 최소화 cost function

학습률 Learning Rate
    너무 크면 Cost Function이 커진다.
    너무 작으면 Epoch가 커진다. (효율성이 떨어진다.)