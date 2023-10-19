num = int(input("홀수를 입력하시오 :"))

blank = (num//2)+1
star = num - ( 2 * blank )

output = ""

for i in range(blank+1,0,-1):
    output += "0"
    for j in range(star+1):
        output += "#"
    output += "\t"
    print(output)
    
        

print(output)



