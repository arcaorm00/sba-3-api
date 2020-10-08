import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_hub as hub
import util.version_checker as version_checker

class Imdb:
    
    train_data: object = None
    validation_data: object = None
    test_data: object = None
    model: object = None

    def __init__(self):
        version_checker.env_info()

    def hook(self):
        self.get_data()
        self.create_model()
        self.train_model()
        self.eval_model()
        self.debug_model()

    # 훈련 세트를 6대 4로 나눈다.
    # 훈련에 15,000개 샘플, 검증에 10,000개 샘플, 테스트에 25,000 샘플 사용
    def get_data(self):
        # train_validation_split = tfds.Split.TRAIN.subsplit([6, 4])
        # https://github.com/tensorflow/datasets/issues/1998 (버전 이슈로 위 코드 사용 불가)
        # https://www.tensorflow.org/datasets/splits ==> 참고
        self.train_data, self.validation_data, self.test_data = tfds.load(
            name="imdb_reviews", 
            split=('train[:60%]', 'train[60%:]', 'test'),
            as_supervised=True
        )

    # 샘플 생성
    # 데이터셋이 많으므로 GD(경사하강법) 보다는 mini-batch 방식을 사용하기 위함
    def create_sample(self) -> object:
        trian_example_batch, train_labels_batch = next(iter(self.train_data.batch(10)))
        return trian_example_batch
    
    # 모델 생성 (교과서 p.507)
    # Dense: 완전 연결층
    def create_model(self):
        embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
        hub_layer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=True)
        hub_layer(self.create_sample()[:3])
        model = tf.keras.Sequential()
        model.add(hub_layer)
        model.add(tf.keras.layers.Dense(16, activation='relu'))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid')) # output
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model = model

    # 모델 훈련
    def train_model(self):
        self.model.fit(self.train_data.shuffle(10000).batch(512), epoch=20, 
        validation_data=self.validation_data.batch(512), verbose=1) # 512 = 2 ^9
    
    # 모델 평가
    def eval_model(self):
        results = self.model.evaluate(self.test_data.batch(512), verbose=2)
        for name, value in zip(self.model.metrics_name, results):
            print('%s: %.3f' % (name, value))

    # 모델 디버깅
    def debug_model(self):
        print(f'self.train_data: {self.train_data}')
        print(f'self.validation_data: {self.validation_data}')
        print(f'self.test_data: {self.test_data}')

if __name__ == '__main__':
    api = Imdb()
    api.hook()
    