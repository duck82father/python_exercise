output = ""

num = int(input("홀수를 입력하시오 :"))
repeat = (num//2)+1

for i in range(repeat, 0, -1):
    for j in range(repeat-1):
        output += " "
    for k in range(0, num, 2):
        output += "*"
    output += "\n"
    

print(output)
