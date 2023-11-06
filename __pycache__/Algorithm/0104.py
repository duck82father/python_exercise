num = 1000000
prime = [True] * (num+1)    # 리스트와 곱셈을 이용해 리스트 뻥튀기 하기!

prime[0], prime[1] = False, False

for i in range(2,num+1):
    if prime[i]:
        for j in range(i*2, num+1, i):  # 2i부터 3i, 4i, 5i...
            prime[j] = False

result = 0
for i in range(num+1):
    if prime[i]:
        result += 1

print(f'2부터 {num} 까지 소수는 총 {result}개 있습니다.')