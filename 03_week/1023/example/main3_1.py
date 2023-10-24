# import cal_sum, cal_sub, cal_mul, cal_div
# import cal_circle

text=input("수식을 입력하시오 > ")
len_text = len(text)
nums=[]
charactors=[]
check='off'

def classification(text, len_text):
    for i in range(len_text):
        global check
        char = text[i]
        if check == 'on':
            charactors.append(str(text[i-1])+str(text[i]))
            check="off"
            if i == (len_text-1):
                return charactors
        elif i == (len_text-1):
            charactors.append(char)
            return charactors
        elif char == "+" or char == "-" or char == "*" or char =="/" or char =="(" or char == ")":
            charactors.append(char)
        elif text[i+1] == "+" or text[i+1] == "-" or text[i+1] == "*" or text[i+1] =="/" or text[i+1] =="(" or text[i+1] == ")":          
            charactors.append(char)
        else:
            check='on'

print(classification(text, len_text))        
        












        
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

# answer = cal_circle.like(len_txt, nums, cal, solv)

# print(answer)