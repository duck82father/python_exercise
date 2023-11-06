import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 프레임 생성
# 학생ID, 나이, 성별, 선호하는 활동으로 구성된 데이터 프레임을 만듭니다.
data = {
    '학생ID': range(1, 101),
    '나이': [8, 11, 7, 12] * 25,
    '성별': ['남', '여'] * 50,
    '선호하는 활동': ['독서', '그림 그리기', '운동', '독서'] * 25
}
df = pd.DataFrame(data)

# 특성과 타겟 분리
# 나이와 성별을 독립 변수로, 선호하는 활동을 종속 변수로 분리합니다.
X = df[['나이', '성별']].copy()
y = df['선호하는 활동'].copy()

# 성별을 숫자로 변환
# 성별을 범주형에서 수치형 데이터로 변환합니다. '남'은 0으로, '여'는 1로 매핑합니다.
print(X)
X['성별'] = X['성별'].map({'남': 0, '여': 1})
print(X)

# 훈련 및 테스트 세트 분할
# 데이터를 훈련 세트와 테스트 세트로 분할합니다. 여기서는 80%를 훈련용, 20%를 테스트용으로 설정합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 의사결정 트리 모델 생성 및 훈련
# 엔트로피를 기준으로 하는 의사결정 트리 분류기를 생성하고, 훈련 데이터로 모델을 훈련합니다.
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train, y_train)

# 예측 및 정확도 평가
# 테스트 세트를 사용하여 예측을 수행하고, 실제값과 예측값을 비교하여 정확도를 계산합니다.
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 정확도 출력
# 모델의 정확도를 출력합니다.
print(f'Accuracy: {accuracy}')


# 각 특성의 중요도 출력
feature_importances = clf.feature_importances_
print(f'Feature importances: {feature_importances}')

# 중요도와 함께 특성 이름 출력
for name, importance in zip(X.columns, feature_importances):
    print(f'{name}: {importance}')



# 결과값
# Accuracy: 1.0
# Feature importances: [1. 0.]
# 나이: 1.0
# 성별: 0.0
