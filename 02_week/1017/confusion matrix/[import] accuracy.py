# 예제 사용법
y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 0]


# 정확도 계산 함수
def accuracy(y_true, y_pred):
    """정확도 계산 함수

    Parameters:
    - y_true: 실제 라벨 리스트
    - y_pred: 모델이 예측한 라벨 리스트

    Returns:
    - 정확도
    """
    correct = sum(true == pred for true, pred in zip(y_true, y_pred))  # *** zip() 공부해! ***
    return correct / len(y_true)


# 출력
print(accuracy(y_true, y_pred))  # 0.8571428571428571 출력 (즉, 85.7% 정확도)

