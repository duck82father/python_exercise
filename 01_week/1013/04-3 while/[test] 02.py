# 2.
# 빈칸을 채워 키와 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리를 만들어 보세요.
# 숫자는 무작위로 입력해도 상관없습니다.

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
charactor = {}

# answer 1 : list comprehension
charactor = {key:i for key, i in zip(key_list, value_list)}
print(charactor)

# answer 2 : for in
charactor = {}
for i in range(len(key_list)):
    charactor[key_list[i]] = value_list[i]

print(charactor)