import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score

# 데이터 읽기
cwd = os.getcwd()
df = pd.read_csv(os.path.join(cwd, "data", "iris.csv"))

# 데이터에서 분별력이 없는 특징(꽃받침의 너비(sepal.width), 꽃잎의 길이(petal.length) 제거
df.drop(["sepal.width", "petal.length"], axis=1, inplace=True)

# 20%의 테스트 데이터 분리
train, test = train_test_split(df, test_size=0.2)

# X_train : features(독립변수) // y_train : label(종속변수; 독립변수를 통해 정해지는 값)
cross_validation_scores = []
X_train = train[['sepal.length', 'petal.width']]
y_train = train[['variety']]

# 최적의 k를 찾기 위해 k의 범위를 3부터 학습 데이터의 절반까지 지정
max_k_range = train.shape[0] // 2
k_list = []

# range([start], stop, [step])를 이용하면 3,5,7 ...
for i in range(3, max_k_range, 2):
    k_list.append(i)

for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train.values.ravel(), cv=5, scoring='accuracy') 
    cross_validation_scores.append(scores.mean())

k = k_list[cross_validation_scores.index(max(cross_validation_scores))]

# knn 알고리즘에 위에서 구한 K값 적용
knn = KNeighborsClassifier(n_neighbors=k)

# knn 모델학습에 train 데이터 적용
knn.fit(X_train, y_train.values.ravel())

# 타겟 데이터 입력
sepal_length = float(input("꽃받침의 너비 입력 (범위: 3.0 ~ 8.0) > "))
petal_width = float(input("꽃잎의 길이 입력 (범위: 0.1 ~ 2.5) > "))

input_target = pd.DataFrame({
	'sepal.length': [sepal_length],
	'petal.width': [petal_width],
})

# knn 알고리즘에 타겟 데이터를 넣어 예측값 출력
pred = knn.predict(input_target)

# 합산 데이터(전체 데이터 + 타켓 데이터) 만들기
input_target['variety'] = ['Target']
new_df = pd.concat([df, input_target], ignore_index=True)

# 합산 데이터로 그래프 만들기
sns.lmplot(x='sepal.length', y='petal.width', data=new_df, fit_reg=False, scatter_kws={"s":120}, markers=["o", "o", "o", "X"], hue="variety",)
plt.title("Sepal length and Petal width of Iris(Setosa, Versicolor, Virginia)") # 그래프의 제목을 설정

plt.show()  # 그래프를 화면에 표시

# 결과값 출력
print("포지션 예측: ", pred)