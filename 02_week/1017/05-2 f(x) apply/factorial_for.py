# 함수 선언
def factorial(n):
    # 변수 선언
    output = 1
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(1, n+1):
        output *= i
    # 리턴
    return output

# 함수 호출
for i in range(1,6):
    print(f"{i}!: ", factorial(i))