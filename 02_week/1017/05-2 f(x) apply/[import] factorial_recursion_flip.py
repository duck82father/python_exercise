# 함수 선언 ( 5! = 1 * 2 * 3 * 4 * 5 )
def factorial_flip(n, s=1):

    # 1 일때
    if n == 0:
        return 1

    # 종료 조건
    if s == n:
        return s

    return s * factorial_flip(n, s+1)

print(factorial_flip(5))
