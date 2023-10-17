def print_t_times(value, n=2):
    # n번 반복
    for i in range(n):
        print(value)

# 함수 호출
print_t_times("안녕하세요", 10)
print_t_times(n=5, value="다른 문구")
print_t_times(n=3) # 매개변수값이 없어 에러가 생김
