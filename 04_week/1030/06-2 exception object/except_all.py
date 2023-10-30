# 변수 선언
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외 처리
try:
    # 숫자 입력
    number_input = int(input("정수 입력 > "))
    # 리스트 요소 출력
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()

except ValueError as exception:
    # ValueError 발생
    print("정수를 입력해주세요")
    print(type(exception), exception)

except IndexError as exception:
    # ValueError 발생
    print("리스트 인덱스를 벗어났어요")
    print(type(exception), exception)

except Exception as exception:
    # 이외의 예외가 발생
    print("예상치 못한 예외가 발생했습니다")
    print(type(exception), exception)

finally:
    print("어찌됐든 수고")