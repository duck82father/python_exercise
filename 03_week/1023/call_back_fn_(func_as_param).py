# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("hello")

# 조합하기
call_10_times(print_hello)

print()

# 실험 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def my_fn(fn):
    for i in range(5):
        fn(i)

def print_annyung(count):
    print("{}번째, 안녕하세요".format(count+1))

def hello2():
    pass

funtions = [print_annyung, hello2]
print(type(funtions))
print(funtions)
print()

funtions_tuple = (print_annyung, hello2)
print(type(funtions_tuple))
print(funtions_tuple)
print()

my_fn(funtions[0])