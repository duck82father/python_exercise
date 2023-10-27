# test.py

# 모델 테스트
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import learn05 as learn

x_train = learn.x_train
y_train = learn.y_train

test = learn.test

k = learn.k

knn = KNeighborsClassifier(n_neighbors=k)


# =========================================================================================================

# knn 모델학습
knn.fit(x_train, y_train.values.ravel())

# 테스트에 사용될 속성 지정
x_test = test[['3P', 'BLK', 'TRB']]

# 선수 포지션에 대한 정답을 지정
y_test = test[['Pos']]

# 테스트 시작
pred = knn.predict(x_test)

# 모델 예측 정확도 출력
print("accuracy: " + str(accuracy_score(y_test.values.ravel(), pred)))

# 예측된 값을 출력해 확인
comparison = pd.DataFrame({'prediction': pred, 'ground_truth': y_test.values.ravel()})
print(comparison)


# 출력값 ===================================================================================================

# PS D:\c402\python> & C:/Users/YONSAI/AppData/Local/Programs/Python/Python312/python.exe d:/c402/python/algorithm/kNN/test1.py
# accuracy: 0.9

#    prediction ground_truth
# 0          SG           SG
# 1           C            C
# 2           C            C
# 3           C            C
# 4          SG           SG
# 5          SG            C
# 6          SG           SG
# 7          SG           SG
# 8          SG           SG
# 9           C            C
# 10         SG           SG
# 11         SG           SG
# 12          C            C
# 13         SG           SG
# 14         SG           SG
# 15         SG           SG
# 16          C            C
# 17          C           SG
# 18         SG           SG
# 19         SG           SG
