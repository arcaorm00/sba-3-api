import os

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

print(tf.version.VERSION)

class FashionMnist:

    def __init__(self):
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def hook(self): 
        image_list = self.get_data()
        self.preproccess(image_list[0], image_list[1])
        model = self.create_model()
        model = self.train_model(model, image_list[0], image_list[1])
        model = self.test_model(model, image_list[2], image_list[3])
        self.model_predict(model, image_list[2], image_list[3], 0)

    def get_data(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

        print(f'훈련 데이터 행 {train_images.shape[0]} / 열 {train_images.shape[1]}')
        print(f'테스트 데이터 행 {test_images.shape[0]} / 열 {test_images.shape[1]}')

        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False)
        plt.show()

        return [train_images, train_labels, test_images, test_labels]

    def preproccess(self,train_images, train_labels):
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_names[train_labels[i]])
        plt.show()

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

        return model

    def train_model(self, model, train_images, train_labels):
        model.fit(train_images, train_labels, epochs=5)
        return model

    def test_model(self, model, test_images, test_labels):
        test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
        print(f'\n테스트 정확도: {test_acc}')
        return model

    def model_predict(self, model, test_images, test_labels, index):
        predictions = model.predict(test_images)
        pred = predictions[index]
        answer = test_labels[index]
        print(f'모델의 예측 값: {np.argmax(pred)}')
        print(f'정답: {answer}')


if __name__ == '__main__':
    fashion = FashionMnist()
    fashion.hook()
    