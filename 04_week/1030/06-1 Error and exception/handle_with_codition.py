# 숫자 입력
user_input_a = input("정수 입력>")

# 사용자 입력이 숫자로만 구성되었을때
if user_input_a.isdigit():
    # 숫자 반환
    number_input_a = int(user_input_a)
    # 출력
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", 2*3.14*number_input_a)
    print("원의 너비 :", 3.14*number_input_a**2)
else:
    print("정수를 입력하지 않았습니다.")