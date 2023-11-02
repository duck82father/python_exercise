from string import ascii_lowercase
from math import ceil, log2

text = ascii_lowercase              # 알파벳 (abcdefghijklmnopqrstuvwxyz)
text_length = len(text)             # 26
number_H = ceil(log2(text_length))  # H값 = 4.7(log2(26))의 올림 숫자 = '5'
char_binary = ""                    # 결과를 담을 2진법 분류 숫자

# 함수
def to_binary(text, text_length, target):
    global char_binary

    if len(text) == 1:
        while len(char_binary) == 4:
            char_binary += '1'
        return char_binary

    # 알파벳 앞쪽 절반(오름차순 기준)에 target 글자가 있을 경우 1 추가
    elif target in text[0:round(text_length/2)]:
        text = text[0:round(text_length/2)]
        text_length = round(text_length/2)
        char_binary += '1'
        to_binary(text, text_length, target)    # target이 포함된 알파벳 절반을 매개변수로 전달
        return char_binary                      # 결과 값(2진법 분류 숫자) 반환

    # 알파벳 뒷쪽 절반('알파벳 전체' - '알파벳 앞쪽 절반(오름차순 기준)')에 target 글자가 있을 경우 0 추가
    elif target in text.replace(text[0:round(text_length/2)], ""):
        text = text.replace(text[0:round(text_length/2)], "")
        text_length = round(text_length/2)
        char_binary += '0'
        to_binary(text, text_length, target)    # target이 포함된 알파벳 절반을 매개변수로 전달
        return char_binary                      # 결과 값(2진법 분류 숫자) 반환


# 결과 도출 (문자 입력)
while True:
    try:
        target = input("\n* 확인할 알파벳 입력해주세요. (전체보기 = 'all' / 끝내기 = 'quit') : ").lower()
        
        if target == 'all':
            for target in text:
                print(target, to_binary(text, text_length, target), sep=" > ", end="\t ")
                char_binary = ""
            continue
        if target == 'quit':
            break
        if target in "":
            raise
        if target not in ascii_lowercase:
            raise
        print("\033[32m"+f"> {target.upper()}"+"\033[0m"+"의 2진법 수는 : "+"\033[32m"+f"{to_binary(text, text_length, target)} "+"\033[0m"+"입니다.")
        char_binary = ""
    
    except:
        print('> '+'\033[96m'+'알파벳을 정확히 입력해주세요 (A-Z, a-z)'+'\033[0m')


    
