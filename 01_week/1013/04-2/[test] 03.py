# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = ["가",1,2,6,8,4,"가",3,2,1,9,5,4,"가",9,7,2,1,"가",3,5,4,8,9,7,2,3]
counter = {}

for num in numbers:
    if num not in counter:  # 딕셔너리에 key 값이 없을 경우 key 값을 1로 넣어서 생성
        counter[num] = "가"
    else:
        counter[num] = counter[num] + 1

print(counter)