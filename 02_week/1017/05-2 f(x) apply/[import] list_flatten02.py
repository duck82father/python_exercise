example = [[1,2,3],[4,[5,6]],7,[8,9]]

def flatten(data):
    # 'output' 변수는 함수 내에서만 생성되고 return될 시 소멸된다.
    output = []
    for item in data:
        if type(item) == list:          # '리스트([])'라면 리스트 안으로 들어가! (요소가 나올 때까지)
            output += flatten(item)
        else:                           # '요소'라면, 더해!
            output.append(item)    
    return output


print("원본: ", example)
print("변환: ", flatten(example))