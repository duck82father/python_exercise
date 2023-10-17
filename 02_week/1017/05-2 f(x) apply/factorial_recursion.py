# 함수 선언 ( 5! = 5 * 4 * 3 * 2 * 1 )
def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    # n이 0이 아니라면 n * (n-1)!을 리턴
    else:
        return n * factorial(n-1)
    
for i in range(1,6):
    print(f"{i}!: ", factorial(i))