import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf
from tensorflow import keras
import util.version_checker as version_checker

class SaveLoad:
    
    train_images: object = None
    train_labels: object = None
    test_images: object = None
    test_labels: object = None

    def __init__(self):
        version_checker.env_info()

    def hook(self):
        self.get_data()
        self.create_model()
        self.train_model()
        self.eval_model()

    def get_data(self):
        (self.train_images, self.train_labels), (self.test_images, self.test_labels)\
             = tf.keras.datasets.mnist.load_data()
        self.train_labels = self.train_labels[:1000]
        self.test_labels = self.test_labels[:1000]
        self.train_images = self.train_images[:1000].reshape(-1, 28*28)/255.0
        self.test_images = self.test_images[:1000].reshape(-1, 28*28)/255.0

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            keras.layers.Dense(512, activation='relu', input_shape=(784, )),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def train_model(self):
        checkpoint_path = 'training_1/cp.ckpt'
        cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, verbose=1)
        self.model.fit(self.train_images, self.train_labels, epochs=10, 
        validation_data = (self.test_images, self.test_labels), callbacks=[cp_callback]) # 훈련 단계 콜백 전달
        self.model.load_weights(checkpoint_path) # 가중치 추가
        loss, acc = self.model.evaluate(self.test_images, self.test_labels, verbose=2)
        print('복원된 모델의 정확도: {:5.2f}%' .format(100 * acc))
        # 파일 이름에 에포크 번호를 포함시킨다.
        checkpoint_path = 'training_2/cp-{epoch: o4d}.ckpt'
        checkpoint_dir = os.path.dirname(checkpoint_path)
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            checkpoint_path, verbose = 1, save_weights_only=True,
            period = 5 # 5번째 에포크마다 가중치를 저장한다.  
        )
        self.model.save_weights(checkpoint_path.format(epochs=0))
        self.model.fit(self.train_images, self.train_labels, epochs=50, callbacks=[cp_callback], validation_data=(self.test_images, self.test_labels), verbose=0)

    # 전체 모델을 HDF5 파일로 저장한다.
    def save_model(self):
        self.model.save()
    
    def load_model(self):
        pass

    def debug_model(self):
        print(f'모델정보: {self.model.summary()}')

if __name__ == '__main__':
    api = SaveLoad()
    api.hook()
    

