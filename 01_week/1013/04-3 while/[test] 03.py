# 3.
# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다. 몇을 더할 때 1000을 넘는지 구해보세요.
# 그리고 그때의 값도 출력해 보세요. 다음은 10,000이 넘는 경우를 구한 예입니다.

# 예) 1, 1+2=3, 1+2+3=6, 1+2+3+4=10 ...

limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    sum_value+=i
    i+=1

print("{}를 더할 때 {}을 넘으며, 그때의 값은 {}입니다.".format(i-1, limit, sum_value))