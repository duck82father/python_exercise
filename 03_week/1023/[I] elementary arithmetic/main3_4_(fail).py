import cal_sum, cal_sub, cal_mul, cal_div
import cal_classify_d

# text=input("수식을 입력하시오 > ")
text="105320*10"
len_text = len(text)
print(eval(text))

text_list = cal_classify_d.isthis(text, len_text)
print("> Result :", cal_classify_d.to_calculate(text_list))