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


if __name__ == "__main__":  
    calc = "10*1589*(650+82)"
    calc_char = len(calc)   
    print("\n> 수식 : {}  /  수식의 문자열 수 : {}".format(calc, calc_char))
    
    result=isthis(calc, calc_char)
    print("\n[ 결과값(수와 연산자 분리) ]\n{}\n".format(result))