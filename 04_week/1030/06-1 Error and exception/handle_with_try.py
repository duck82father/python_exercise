# try except 구문으로 예외 처리

try:
    # 숫자 변환
    number_input_a = int(input("정수 입력>"))
    # 출력
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", 2*3.14*number_input_a)
    print("원의 너비 :", 3.14*number_input_a**2)
except:
    print("무언가 잘못되었습니다.")