from string import ascii_lowercase
from math import ceil, log2

text = ascii_lowercase              # abcdefghijklmnopqrstuvwxyz
text_length = len(text)             # 26
number_H = ceil(log2(text_length))  # 5

# selected_text = []                  # 체크할 문자열
char_binary = ""                    # 결과를 담을 2진법 숫자

# target = input("확인할 알파벳을 입력하시오 : ").lower()

print(text[0:26])

def to_binary(text, text_length, target):
    global char_binary

    if len(text) == 1:
        while len(char_binary)==4:
            char_binary += '1'
        return char_binary
        
    elif target in text[0:round(text_length/2)]:
        text = text[0:round(text_length/2)]
        text_length = round(text_length/2)
        char_binary += '1'
        to_binary(text, text_length, target)
        return char_binary

    elif target in text[round(text_length/2):text_length]:
        text = text[round(text_length/2):text_length]
        text_length = round(text_length/2)
        char_binary += '0'
        to_binary(text, text_length, target)
        return char_binary
    
    else:
        char_binary += '000'
        return char_binary

# 전체 검증
for target in text:
    print(target, to_binary(text, text_length, target))
    char_binary = ""

# 결과값
# print("{}의 2진법 수는 : {} 입니다.".format(target, to_binary(text, text_length, target)))
