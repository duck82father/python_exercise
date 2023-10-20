def accuracy(y_true, y_pred):
    """정확도 계산 함수

    Parameters:
    - y_true: 실제 라벨 리스트
    - y_pred: 모델이 예측한 라벨 리스트

    Returns:
    - 정확도

    """
    
    # 1번 > for in / if
    correct_a = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] :
            correct_a += 1
    print(correct_a / len(y_true))


    # 2번 > for in / if / zip(a, b)
    correct_b = 0
    for true, pred in zip(y_true, y_pred) :
        if true == pred :
            correct_b += 1
    print(correct_b / len(y_true))

    
    # 3번 > for in / zip(a, b)
    correct = sum(y_true == y_pred for y_true, y_pred in zip(y_true, y_pred))
    
    return correct / len(y_true)

    

# 예제 사용법
y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 0]
print(accuracy(y_true, y_pred))  # 0.8571428571428571 출력 (즉, 85.7% 정확도)
