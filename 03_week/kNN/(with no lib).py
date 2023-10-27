import math

# 데이터셋
data = [
    (5.1, 3.5, "Setosa"),
    (4.9, 3.0, "Setosa"),
    (6.0, 3.0, "Versicolor"),
    (6.2, 2.8, "Versicolor"),
    (5.5, 2.3, "Versicolor"),
    (6.3, 3.3, "Setosa"),
    (5.8, 2.7, "Versicolor"),
    (6.7, 3.0, "Setosa")
]

# 유클리디안 거리 계산
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# kNN 알고리즘
def kNN(new_point, k=3):
    # 거리 계산
    distances = [(point, distance(new_point, point)) for point in data]
    # 거리에 따라 데이터 정렬
    sorted_neighbors = sorted(distances, key=lambda x: x[1])
    
    # 가장 가까운 k 개의 이웃을 찾기
    k_neighbors = [item[0] for item in sorted_neighbors[:k]]
    
    # 다수결 방식으로 레이블 결정
    from collections import Counter
    vote_counts = Counter([neighbor[2] for neighbor in k_neighbors])
    return vote_counts.most_common(1)[0][0]

# 테스트
new_data = (5.5, 3.0)
print(f"The predicted class of {new_data} is {kNN(new_data)}")
