import cal_sum, cal_sub, cal_mul, cal_div
import cal_classify_f

# text=input("수식을 입력하시오 > ")
text="145-20*3/4+105320*10-1091*50*2/33-19"
len_text = len(text)
print(f"> eval__ : {eval(text)}")   # 문자로 된 수식을 바로 계산해주는 함수 eval()

text_list = cal_classify_f.isthis(text)
print("> Result :", cal_classify_f.to_calculate(text_list))