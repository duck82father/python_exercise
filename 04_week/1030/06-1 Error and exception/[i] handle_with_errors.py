# 예외 처리 방법 3가지

# 01. if 문 사용
user_input = input("정수 입력 > ")
if user_input.isdigit():
    pass
else:
    pass
    # 예외 처리


# 02. try except 사용
try:
    user_input=input("정수 입력 > ")
except:
    pass
    # 예외 처리


# 03. try except + else finally 사용
try:
    user_input=input("정수 입력 > ")
except:
    pass
    # 예외처리
else:
    pass
finally:
    pass