from keras.models import Sequential
from keras.layers import Dense
# from keras.callbacks import ModelCheckpoint, EarlyStopping # 책에 있으나 안씀

import pandas as pd
import numpy
import tensorflow as tf
# import matplotlib.pyplot as plt # 책에 있으나 안씀

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
data_pre = pd.read_csv('dataset/wine.csv', header=None)
data = data_pre.sample(frac = 1)
dataset = data.values
x = dataset[:, 0:12]
y = dataset[:, 12]

# 모델 설정
model = Sequential()
model.add(Dense(30, input_dim = 12, activation = 'relu'))
model.add(Dense(12, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

# 모델 컴파일
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# 모델 실행
model.fit(x, y, epochs = 200, batch_size = 200)

# 결과 출력
print("\n accuracy: %.4f" % (model.evaluate(x, y)[1]))
