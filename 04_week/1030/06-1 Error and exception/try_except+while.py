# 메뉴 1-한식, 2-중식, 3-일식, 4-분식
# 입력 오류 시 "메뉴를 다시 골라주세요"

while True:
    try:    # 예외 발생 시 except 이후 구문 실행
        text = """\n-------------------------------------------------------------
        \n[ 메뉴 ]\n1 - 한식\n2 - 중식\n3 - 일식\n4 - 분식\n\nQ - 종료하기\n"""
        print(text)
        choice = input("메뉴를 선택해주세요 : ")
        if choice == '1':
            print('\n>> 선택하신 메뉴는 \'한식\'입니다')
        elif choice == '2':
            print('\n>> 선택하신 메뉴는 \'중식\'입니다')
        elif choice == '3':
            print('\n>> 선택하신 메뉴는 \'일식\'입니다')
        elif choice == '4':
            print('\n>> 선택하신 메뉴는 \'분식\'입니다')
        else:
            # 예외 발생
            raise
    except:
        if choice.upper() == 'Q':
            print("\n*** 메뉴 선택을 종료합니다 ***\n")
            break
        else:
            print("\n*** 메뉴를 다시 선택해주세요 ***")
