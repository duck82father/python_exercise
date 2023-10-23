import random

# 임의의 문자를 반환
a=random.choice("abc")
print(a)

# 1부터 10사이의 임의의 정수 반환
b = random.randint(1, 10)
print(b)

# 1부터 9까지 목록 반환
c = range(1,10)
print(c)

# 1부터 9까지 반환된 목록 중 임의의 항목 반환
d = random.randrange(1,10)
print(d)