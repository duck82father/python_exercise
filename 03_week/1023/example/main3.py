import cal_sum, cal_sub, cal_mul, cal_div
import cal_circle

text=(input("수식 입력: "))
len_txt = len(text)
nums=[]
charactors=[]
solv=0
count=0

def circle(count):
    while True:
        char = text[count]
        char2 = text[count+1]
        if char != "+" and char != "-" and char != "*" and char !="/" and char !="(" and char != ")":
            if char2 != "+" and char2 != "-" and char2 != "*" and char2 !="/" and char2 !="(" and char2 != ")":
            charactors[count]+=[char]
            circle(count)
        else:
            charactors.append(char)
    
    # elif text[i] == "+":
    #     cal.append(cal_sum.like)
    # elif text[i] == "-":
    #     cal.append(cal_sub.like)
    # elif text[i] == "*":
    #     cal.append(cal_mul.like)
    # elif text[i] == "/":
    #     cal.append(cal_div.like)


    # elif text[i] == "+":
    #     cal.append(cal_sum.like)
    # elif text[i] == "-":
    #     cal.append(cal_sub.like)
    # elif text[i] == "*":
    #     cal.append(cal_mul.like)
    # elif text[i] == "/":
    #     cal.append(cal_div.like)

print(nums)

# answer = cal_circle.like(len_txt, nums, cal, solv)

# print(answer)