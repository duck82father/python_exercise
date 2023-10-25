# 4.
# 1부터 100까지의 숫자가 있다고 합시다. 이를 다음과 같이 계산한다고 했을 때,
# 최대가 되는 경우는 어떤 숫자를 곱했을 때인지를 찾아 주세요.

# 1 * 99, 2 * 98, 3 * 97, 4 * 96, ....

sum_value = 0
next_sum_value = 0

for i in range(1, 100):
    if sum_value > next_sum_value:
        i-=1
        break
    else:
        sum_value = i*(100-i)
        next_sum_value = (i+1)*(99-i)

print("최대가 되는 경우: {} * {} = {}".format(i, 100-i, sum_value))