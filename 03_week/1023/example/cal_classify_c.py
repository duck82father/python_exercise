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
                print("charactors : ", charactors)  # 테스트용 출력
                return charactors
            
            if not_int(text[i+1]):
                charactors.append(memory)
                check="off"

            else:
                memory += text[i]

        elif i == (len_text-1):
            charactors.append(char)
            print("charactors : ", charactors)    # 테스트용 출력
            return charactors

        elif not_int(char):
            charactors.append(char)

        elif not_int(text[i+1]):          
            charactors.append(char)

        else:
            memory=str(text[i])+str(text[i+1])
            check='on'



def plus_minus(new_list, i, mid_sum):

    while True:
        if len(new_list) <= i+3:
            if new_list[i+1] in "+-":
                what_calc_type = cal_type(new_list[i+1])
                sum = what_calc_type.isthis(int(new_list[i]), int(new_list[i+2]))
                return sum

        else:
            if new_list[i+1] in "+-":
                what_calc_type = cal_type(new_list[i+1])
                sum = what_calc_type.isthis(int(new_list[i]), plus_minus(new_list, i+2))
                return sum


def to_calculate(text_list):
    new_list = []
    mid_sum = ''
    pass_check = 0
    
    for i in range(len(text_list)):

        if text_list[i] not in "+-*/()":    # 숫자
            if pass_check == 1:
                pass_check = 0
                pass
            elif text_list[i-1] == "-":
                new_list.append(int(text_list[i])*-1)
            else:
                new_list.append(int(text_list[i]))
                mid_sum = text_list[i]
        # elif i==range(len(text_list)-1):
        #     new_list.append(text_list[i])
        
        if text_list[i] in "*/":    # 곱셈, 나눗셈
            what_calc_type = cal_type(text_list[i])
            mid_sum = what_calc_type.isthis(int(mid_sum), int(text_list[i+1]))
            del new_list[-1]
            new_list.append(mid_sum)
            pass_check = 1

        # elif text_list[i] in "+":    # 덧셈
        #     new_list.append(text_list[i])
        
        # elif text_list[i] in "-":    # 뺄셈
        #     new_list.append(text_list[i])


    print("new_list : ", new_list)

    final = 0
    
    for j in new_list:
        final += j
        return final
    
    print("final : ", final)

    return final
    



if __name__ == "__main__":  
    
    # calc = "10*1589*(650+82)"
    # calc_char = len(calc)   
    # print("\n> 수식 : {}  /  수식의 문자열 수 : {}".format(calc, calc_char))
    
    # result_text=isthis(calc, calc_char)
    # print("\n[ 결과값(수와 연산자 분리) ]\n{}\n".format(result_text))

    # text_list = ['10', '+', '100', '*', '(', '2', '+', '500', ')']
    # text_list = ['2', '*', '2', '*', '3', '-', "3", "+", "4"]
    text_list = ['100', '+', '100', '*', '3', '-', '25', '*', '2', '*', '2', '+', '7', '*', '3']
    result_cal = to_calculate(text_list)

    print(text_list)
    print(result_cal)
    # print(plus_minus([100, '+', 300, '-', 100, '+', 21], 0))