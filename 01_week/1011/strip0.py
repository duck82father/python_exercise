# 예제 0

input_a = """
     안녕하세요
문자열의 함수를 알아봅시다
"""

print(input_a.strip())


# 예제 -1

# 양 옆의 공백 제거
name = input("입력(공백 여부 상관없음)> ")

# 입력 값을 통한 출력(공백 제거 여부 확인)
print("양 옆 공백 제거: {}".format(name.strip()))
print("공백 제거 없이: {}".format(name))