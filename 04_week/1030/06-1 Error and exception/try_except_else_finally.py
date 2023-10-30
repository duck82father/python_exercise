# try except 구문으로 예외 처리

try:
    # 숫자 변환
    number_input_a = int(input("정수 입력> "))
    # 출력
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", 2*3.14*number_input_a)
    print("원의 너비 :", 3.14*number_input_a**2)
except:
    except_check = 1
    print("!오류! 정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("- - - [결과보고] - - -\n프로그램이 어떻게든 끝났습니다.\n한번 더 기회를 드리겠습니다.")
    try:
        # 숫자 변환
        number_input_a = int(input("다시 한 번, 정수 입력> "))
        # 출력
        print("원의 반지름 :", number_input_a)
        print("원의 둘레 :", 2*3.14*number_input_a)
        print("원의 너비 :", 3.14*number_input_a**2)
    except:
        if except_check==1:
            print("또 틀리셨다니 유감입니다.")
    else:
        print("예외가 발생하지 않았습니다.")
    finally:
        print("- - - [결과보고] - - -\n프로그램이 어떻게든 끝났습니다.\n수고하셨습니다.")