# range(2, 10) = [2, 3, 4, 5, 6, 7, 8, 9]

for i in range(2, 10):
    print(f"\n{i}단")
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")


# 입력된 단수의 구구단만 출력

num = int(input("\n알고 싶은 구구단 수를 입력하시오 >"))

print(f"\n{num}단")
for k in range(2, 10):
    print(f"{num} * {k} = {num*k}")


print()

# 구구단 출력
# 각 단을 가로로 출력
for i in range(1, 10):  # 1부터 9까지 반복
    for j in range(2, 10):  # 2단부터 9단까지 반복
        result = j * i
        print(f"{j}x{i}={result}", end='\t')  # 탭 문자로 구분
    print()  # 각 행의 끝에 줄 바꿈 문자 출력