import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

import learn05_data_preprocessing as learn

x_train = learn.x_train
y_train = learn.y_train

test = learn.test

k = learn.k

knn = KNeighborsClassifier(n_neighbors=k)

# knn 모델학습
knn.fit(x_train, y_train.values.ravel())

# 예측할 데이터
# 새로 영입하는 농구선수의 3P, BLK, TRB 결과가 1.4, 0.1, 1.3으로 가정
x_new = pd.DataFrame({
	'3P': [1.4],
	'BLK': [0.1],
	'TRB': [1.3]
})

pred = knn.predict(x_new)

print("포지션 예측: ", pred)