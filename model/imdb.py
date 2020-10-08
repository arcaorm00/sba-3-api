import numpy as np
import tensorflow as tf
import tensorflow_dataset as tfds

class Imdb:
    
    train_data: object = None
    validation_data: object = None
    test_data: object = None
    model: object = None

    def hook(self):
        pass

    # 훈련 세트를 6대 4로 나눈다.
    # 훈련에 15,000개 샘플, 검증에 10,000개 샘플, 테스트에 25,000 샘플 사용
    def get_data(self):
        pass

    # 샘플 생성
    # 데이터셋이 많으므로 GD(경사하강법) 보다는 mini-batch 방식을 사용한다.
    def create_sample(self) -> object:
        return None
    
    # 모델 생성
    def create_model(self):
        self.model = model

    # 모델 훈련
    def train_model(self):
        self.model.fit()
    
    # 모델 평가
    def eval_model(self):
        self.model.evaluate()