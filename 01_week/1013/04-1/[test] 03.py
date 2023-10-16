numbers = [127, 34, 358, 18, 65, 178, 99, 1005, 100]

# 홀/짝 구분
for number in numbers:
    if number % 2 == 1:
        print(f"{number}는 홀수입니다.")
    else:
        print(f"{number}는 짝수입니다.")

print()

# 자리수 구하기
for number in numbers:
    print(f"{number}는 {len(str(number))}자리수입니다.")