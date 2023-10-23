import random

def IA(count):
    for i in range(count):
        global winner
        global timeis
        if count==1:
            return winner         
        num = random.randrange(10)+1
        if winner[num] == "IA":
            IA(count)
        else:
            winner[num]="IA"
            IA(count-1)



winner = {}
for i in range(10):
    winner[i+1]=""

count=0
timeis=""

print(IA(3))

# for i in range(1, 4):
#     num = random.randrange(10)+1
#     if winner[num] == "IA" or winner[num] == "HC":
#         i = i-1
#         pass
#     else:
#         winner[num]="HC"

# for i in range(1,5):
#     num = random.randrange(10)+1
#     if winner[num] == "IA" or winner[num] == "HC" or winner[num] == "CP":
#         i = i-1
#         pass
#     else:
#         winner[num]="CP"

# print(winner)