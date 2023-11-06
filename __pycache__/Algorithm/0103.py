# 1은 소수가 아니므로 제외

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = 1000000
result = 0

for i in range(2, n+1):
    if is_prime(i):
        result += 1

print(n, result)