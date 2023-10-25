import cal_sum, cal_sub, cal_mul, cal_div

nums=[]
items=[]
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
    
# 수식을 item(숫자, 산술기호)로 개별 분리, 2자리 이상의 숫자일 경우 합쳐서 읽기
def isthis(text, len_text):
    for i in range(len_text):
        
        global check
        global memory
        char = text[i]

        if check == 'on':
            if i == (len_text-1):
                items.append(memory)
                print("> items :", items)  # 테스트용 출력
                return items
            
            if not_int(text[i+1]):
                items.append(memory)
                check="off"

            else:
                memory += text[i]

        elif i == (len_text-1):
            items.append(char)
            print("> items_ :", items)    # 테스트용 출력
            return items

        elif not_int(char):
            items.append(char)

        elif not_int(text[i+1]):          
            items.append(char)

        else:
            memory=str(text[i])+str(text[i+1])
            check='on'


def mid_list_add(text_list, i):
    mid_list=[]
    j=0
    while True:
        j+=1
        if text_list[i+j]==")":
            return mid_list
        else:
            mid_list.append(text_list[i+j])


# isthis()함수에서 나온 items를 가져와 곱셈, 나눗셈은 미리 계산하고, 뺄셈일 경우 다음 숫자에 -1을 곱하여 정리
# 마지막으로 위에서 계산된 값을 더하여 결과를 return
def to_calculate(text_list):
    print('text_list', text_list)
    new_list = []
    mid_sum = ''
    mid_list = []
    pass_check = 0
    
    for i in range(len(text_list)):

        if pass_check == 2 :
            if text_list[i] == ")":
                new_list.append(mid_sum)
                pass_check = 1
            else:
                continue
            
        elif text_list[i] in "(":
            mid_list = mid_list_add(text_list, i)
            print('mid_lst', mid_list)
            mid_sum = to_calculate(mid_list)
            print('mid_sum', mid_sum)
            pass_check = 2

        else :
            if pass_check == 1:                                 # 1. pass_check == 1 일때, mid_sum 값이 있음을 의미
                pass_check = 0                                  # mid_sum이 있을 경우 곱셈 또는 나눗셈 계산중이니 숫자를 더하는 과정을 pass함
                continue
            
            else:                                               # 2. pass_check == 0 일때, 숫자를 더하는 과정을 진행
                if text_list[i] not in "+-*/":                  
                    if text_list[i-1] == "-":
                        new_list.append(int(text_list[i])*-1)
                        mid_sum = int(text_list[i])*-1
                    else:
                        if text_list[i-1] == ")":
                            new_list.append(mid_sum)
                        else:
                            new_list.append(int(text_list[i]))
                            mid_sum = int(text_list[i])         
            
            if text_list[i] in "*/":                            # 3. 곱셈의 과정일 경우 이전 수와 다음의 수를 계산
                what_calc_type = cal_type(text_list[i])
                mid_sum = what_calc_type.isthis(int(mid_sum), int(text_list[i+1]))
                del new_list[-1]
                new_list.append(mid_sum)
                pass_check = 1

    print("> short_ :", new_list)

    final = 0  
    for j in new_list:
        final += j

    print('final', final)
    return final
    

if __name__ == "__main__":  
    
    # text_list = ['100', '+', '100', '*', '3', '-', '25', '*', '2', '*', '2', '+', '7', '*', '3']
    # text_list = ['5','+','(','1','+','1',')','+','1']
    text_list = ['5','-','(','1','+','1',')','+','1']
    # text_list = ['5','*','(','1','+','1',')','+','1']
    result_cal = to_calculate(text_list)

    print(result_cal)