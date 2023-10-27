def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # error


gen = (x ** 2 for x in range(5))
for val in gen:
    print(val)  # 0, 1, 4, 9, 16을 순차적으로 출력

# 예3 무한 시퀀스 생성
def count_up():
    count = 0
    while True:
        yield count
        count += 1