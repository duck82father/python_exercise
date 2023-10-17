# 예제 사용법
y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 1, 1]


def precision(y_true, y_pred):
    """정밀도 계산 함수

    Parameters:
    - y_true: 실제 라벨 리스트
    - y_pred: 모델이 예측한 라벨 리스트

    Returns:
    - 정밀도
    """
    TP = sum(true == 1 and pred == 1 for true, pred in zip(y_true, y_pred))
    FP = sum(true == 0 and pred == 1 for true, pred in zip(y_true, y_pred))
    
    if TP + FP == 0:
        return 0  # 분모가 0이 되는 경우를 피하기 위해 정밀도를 0으로 설정
    
    return TP / (TP + FP)


print(precision(y_true, y_pred))  # 0.6 출력 (즉, 60% 정밀도)

