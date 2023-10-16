# 함수 정의
def return_test_A():
    print("A위치입니다.")
    return
    print("B위치입니다.")

def return_test_B():
    print("A위치입니다.")
    return print("B위치입니다.")

# 함수 호출
return_test_A()

print()

return_test_B()