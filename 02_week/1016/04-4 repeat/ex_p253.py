number = [1, 2, 3, 4, 5, 6]

rev_number = reversed(number)

for i in rev_number:
    print("A의 첫번째 반복문 : {}".format(i))

print()

for i in rev_number:
    print("A의 두번째 반복문 : {}".format(i))

print()

for i in reversed(number):
    print("B의 첫번째 반복문 : {}".format(i))

print()

for i in reversed(number):
    print("B의 두번째 반복문 : {}".format(i))