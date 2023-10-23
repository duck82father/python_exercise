# Q.

# 커피종류, 수량 = {"IA":10, "HC":50, "CP":40,}

# 전화번호 1 ~ 100번까지 있을 때
# 랜덤하게 당첨시키는 프로그램

# - - - - - - - - - - - - - - - - - - - - - - 

# S.

# 1. 당첨자 dict에, 임의의 10개 key는 IA, 그 다음 임의의 50개 키에는 HC, 그 다음 임의의 40개 키에 CP 값을 넣는다.
# 2. 임의의 키를 넣을때(for문), 숫자 key값에 이미 값이 있다면(if문) pass, 없다면 값 추가.


import random

winner = {}
count=0

for i in range(100):
    winner[i+1]=""

for i in range(1, 11):
    num = random.randrange(100)+1
    if winner[num] == "IA":
        i = i-1
        pass
    else:
        winner[num]="IA"

for i in range(1, 51):
    num = random.randrange(100)+1
    if winner[num] == "IA" or winner[num] == "HC":
        i = i-1
        pass
    else:
        winner[num]="HC"

for i in range(1,41):
    num = random.randrange(100)+1
    if winner[num] == "IA" or winner[num] == "HC" or winner[num] == "CP":
        i = i-1
        pass
    else:
        winner[num]="CP"

print(winner)