import cal_sum, cal_sub, cal_mul, cal_div

nums=[]
charactors=[]
check='off'
memory=''

def not_int(char):
    if char in "+-*/()":
        return True
    else:
        return False

def cal_type(cal_type):
    if cal_type == "+":
        return cal_sum
    if cal_type == "-":
        return cal_sub
    if cal_type == "*":
        return cal_mul
    if cal_type == "/":
        return cal_div
    
def isthis(text, len_text):
    for i in range(len_text):
        
        global check
        global memory
        char = text[i]

        if check == 'on':
            if i == (len_text-1):
                charactors.append(memory)
                return charactors
            
            if not_int(text[i+1]):
                charactors.append(memory)
                check="off"

            else:
                memory += text[i]

        elif i == (len_text-1):
            charactors.append(char)
            return charactors

        elif not_int(char):
            charactors.append(char)

        elif not_int(text[i+1]):          
            charactors.append(char)

        else:
            memory=str(text[i])+str(text[i+1])
            check='on'


def to_calculate(text_list, i=0):

    while True:
        if i==len(text_list):
            if text_list[i] == ")":
                return
            else:
                return text_list[i]

        elif text_list[i] == ")":
            what_calc_type = cal_type(text_list[i+1])
            sum = what_calc_type.isthis(int(text_list[i]), int(text_list[i+2]))
            return sum
                
        if len(text_list) > i+3:
            if text_list[i+2] in "(":
                new_list=[]
                for j in text_list[i+3:len(text_list)]:
                    if j == ")":
                        break
                    else:
                       new_list.append(j)
                what_calc_type = cal_type(text_list[i+1])
                sum = what_calc_type.isthis(int(text_list[i]), to_calculate(new_list))
                return sum

        if len(text_list) <= i+3:
            if text_list[i+1] in "*/":
                what_calc_type = cal_type(text_list[i+1])
                sum = what_calc_type.isthis(int(text_list[i]), int(text_list[i+2]))
                return sum

            if text_list[i+1] in "+-":
                what_calc_type = cal_type(text_list[i+1])
                sum = what_calc_type.isthis(int(text_list[i]), int(text_list[i+2]))
                return sum

        else:
            if text_list[i+1] in "*/":
                what_calc_type = cal_type(text_list[i+1])
                sum = what_calc_type.isthis(int(text_list[i]), to_calculate(text_list, i+2))
                return sum

            if text_list[i+1] in "+-":
                what_calc_type = cal_type(text_list[i+1])
                sum = what_calc_type.isthis(int(text_list[i]), to_calculate(text_list, i+2))
                return sum
        


if __name__ == "__main__":  
    
    # calc = "10*1589*(650+82)"
    # calc_char = len(calc)   
    # print("\n> 수식 : {}  /  수식의 문자열 수 : {}".format(calc, calc_char))
    
    # result_text=isthis(calc, calc_char)
    # print("\n[ 결과값(수와 연산자 분리) ]\n{}\n".format(result_text))

    # text_list = ['10', '+', '100', '*', '(', '2', '+', '500', ')']
    text_list = ['2', '*', '2', '*', '3', '-', "3", "+", "4"]
    result_cal = to_calculate(text_list)

    print(text_list)
    print(result_cal)