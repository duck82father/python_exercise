def char_to_binary(char):
    # 알파벳을 0-25 사이의 숫자로 매핑합니다.
    char = char.upper()  # 대문자로 변환
    if not ('A' <= char <= 'Z'):  # 문자가 A-Z 범위에 없으면 예외 발생
        raise ValueError("문자 A-Z을 입력해 주세요.")
    num = ord(char) - ord('A')

    # 이진 검색으로 각 비트를 결정합니다.
    binary_code = ''
    low, high = 0, 25
    for _ in range(5):  # 알파벳을 나타내는데 5비트 필요
        mid = (low + high) // 2
        if num <= mid:
            binary_code += '1'
            high = mid
        else:
            binary_code += '0'
            low = mid + 1

    return binary_code

def word_to_binary(word):
    return ''.join(char_to_binary(char) for char in word)

# 예시 단어로 테스트
test_word = "HELLO"
binary_word = word_to_binary(test_word)
print(f"입력한 단어 '{test_word}'의 binary는 {binary_word}입니다.")