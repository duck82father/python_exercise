# scikit-learn(sklearn) 설치
# 파이썬에서 머신 러닝 및 데이터 과학 작업을 수행하기 위한 강력한 라이브러리
# pip install scikit-learn

# 필요한 라이브러리 불러오기
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 꽃의 특성 데이터 (꽃받침 길이와 꽃받침 너비)
X = np.array([[5.1, 3.5],
              [4.9, 3.0],
              [6.0, 3.0],
              [6.2, 2.8],
              [5.5, 2.3],
              [6.3, 3.3],
              [5.8, 2.7],
              [6.7, 3.0]])

# 꽃의 종류 (0: Setosa, 1: Versicolor)
y = np.array([0, 0, 1, 1, 1, 0, 1, 0])

# KNN 모델 생성 (K=3로 설정)
knn = KNeighborsClassifier(n_neighbors=3)

# 모델 학습
knn.fit(X, y)

# 새로운 꽃 데이터에 대한 예측
new_flower = np.array([[5.4, 2.8]])
predicted_class = knn.predict(new_flower)

if predicted_class[0] == 0:
    print("Setosa 꽃입니다.")
else:
    print("Versicolor 꽃입니다.")
