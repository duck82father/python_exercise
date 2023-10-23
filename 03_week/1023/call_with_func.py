# 함수 선언
def power(item):
    return item*item
def under_3(item):
    return item < 3

def my_fn():
    print("hello")

my_fn() # Step Into

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filler() 함수 사용
output_b = filter(under_3, list_input_a)
print("# map 함수의 실행 결과")
print("filter(power, list_input_a):", output_b)
print("filter(power, list_input_a):", list(output_b))
print()