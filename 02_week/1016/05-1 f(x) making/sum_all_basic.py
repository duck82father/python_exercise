# 함수 선언
def sum_all(start, end):
    # 변수 선언
    output = 0
    # 반복문으로 숫자 더하기
    for i in range(start, end+1):
        output += i
    # 리턴합니다
    return output

# 함수 호출
print("0 to 100 :", sum_all(0, 100))