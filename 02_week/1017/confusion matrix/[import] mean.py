numbers = [1, 2, 3, 4, 5]

# 산술평균 함수
def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

# 기하평균 함수
def geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

# 조화평균 함수
def harmonic_mean(numbers):
    return len(numbers) / sum(1/num for num in numbers)     # => 1/1 + 1/2 + 1/3 + 1/4 + 1/5

print(arithmetic_mean(numbers))  # 산술평균
print(geometric_mean(numbers))  # 기하평균
print(harmonic_mean(numbers))   # 조화평균