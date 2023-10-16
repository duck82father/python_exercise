# 1. 간단한 대화 프로그램
    
i = input("입력: ")

if "안녕" in i:
    print("안녕하세요.")
elif "몇 시" in i:
    print("지금은 15시입니다.")
else:
    print(i)

#
print()

# 2. 나누어 떨어지는 숫자

num = int(input("정수를 입력해주세요: "))
notice = "로 나누어 떨어지는 숫자"

if (num % 2) == 0 :
    print(f"{num}은 2{notice}입니다")
else:
    print(f"{num}은 2{notice}가 아닙니다")

if (num % 3) == 0 :
    print(f"{num}은 3{notice}입니다")
else:
    print(f"{num}은 3{notice}가 아닙니다")

if (num % 4) == 0 :
    print(f"{num}은 4{notice}입니다")
else:
    print(f"{num}은 4{notice}가 아닙니다")

if (num % 5) == 0 :
    print(f"{num}은 5{notice}입니다")
else:
    print(f"{num}은 5{notice}가 아닙니다")
