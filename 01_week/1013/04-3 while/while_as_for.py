# while 문은 반복 조건은 'true' 일 동안
i = -5
while i < 5:
    print("{}번째 반복입니다.".format(i))
    i += 1

print()

# for 문은 반복 조건은 index 번호를 통한 반복횟수의 카운팅
for j in range(5):
    print("{}번째 반복입니다.".format(j))