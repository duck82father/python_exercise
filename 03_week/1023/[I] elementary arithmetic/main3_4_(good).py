import cal_sum, cal_sub, cal_mul, cal_div
import cal_classify_d

text=input("수식을 입력하시오 > ")
len_text = len(text)

text_list = cal_classify_d.isthis(text, len_text)
print("> Result :", cal_classify_d.to_calculate(text_list))