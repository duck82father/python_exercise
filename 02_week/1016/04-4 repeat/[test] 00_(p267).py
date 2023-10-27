output = [n for n in range(1,101) if f"{n:b}".count('0') == 1]
print(output)

for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계: ", sum(output))