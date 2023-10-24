import cal_sum, cal_sub, cal_mul, cal_div
import cal_classify_c

text=input("수식을 입력하시오 > ")
len_text = len(text)

text_list = cal_classify_c.isthis(text, len_text)
print(cal_classify_c.to_calculate(text_list))


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