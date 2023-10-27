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
def isthis(s):
    
    operators = set('+-*/')     # 연산자

    result = []                 # 문자열 피싱
    number = ""

    for char in s:
        if char in operators:
            if number:
                result.append(int(number))
                number = ""
            result.append(char)
        else:
            number += char

    # 마지막 숫자 추가
    
    if number:
        result.append(int(number))
    
    return result



# isthis()함수에서 나온 items를 가져와 곱셈, 나눗셈은 미리 계산하고, 뺄셈일 경우 다음 숫자에 -1을 곱하여 정리
# 마지막으로 위에서 계산된 값을 더하여 결과를 return

def to_calculate(text_list):
    new_list = []
    mid_sum = ''
    pass_check = 0

    for i in range(len(text_list)):

        if pass_check == 1:                                 # 1. pass_check == 1 일때, mid_sum 값이 있음을 의미
            pass_check = 0                                  # mid_sum이 있을 경우 곱셈 또는 나눗셈 계산중이니 숫자를 더하는 과정을 pass함
            continue
        
        else:                                               # 2. pass_check == 0 일때, 숫자를 더하는 과정을 진행
            if text_list[i] not in "+-*/":                  
                if text_list[i-1] == "-":
                    new_list.append(int(text_list[i])*-1)
                    mid_sum = int(text_list[i])*-1
                else:
                    new_list.append(int(text_list[i]))
                    mid_sum = int(text_list[i])         
        
        if text_list[i] in "*/":                            # 3. 곱셈의 과정일 경우 이전 수와 다음의 수를 계산
            what_calc_type = cal_type(text_list[i])
            mid_sum = what_calc_type.isthis(int(mid_sum), int(text_list[i+1]))
            del new_list[-1]
            new_list.append(mid_sum)
            pass_check = 1

    print("> split_ :", new_list)

    final = 0  
    for j in new_list:
        final += j

    return final
    


if __name__ == "__main__":  
    
    text_list = "1+2*3/4+105320*10-1091*50*2/33-19"
    isthis(text_list)
    # result_cal = to_calculate(text_list)

    # print(result_cal)