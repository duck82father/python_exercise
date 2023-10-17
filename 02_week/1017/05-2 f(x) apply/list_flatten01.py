def flatten(data):
    # 'output' 변수는 함수 내에서만 생성되고 return될 시 소멸된다.
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)    
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본: ", example)
print("변환: ", flatten(example))
print(flatten(flatten(example)))