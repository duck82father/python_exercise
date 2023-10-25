print()

# 딕셔너리를 선언합니다
dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀",
}

# 출력합니다
print("--- 전 항목 출력 ---")
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"][2])
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다
print("--- 변경항목 출력 ---")
dictionary["name"]="8D 건조 망고"
print("name:",dictionary["name"])
print()

# 값을 추가합니다
print("--- 추가항목 출력 ---")
dictionary["price"]=8000
print("price:",dictionary["price"])

# 출력합니다 (개별 항목 하나씩 나열하기)
print("--- 전 항목 출력 (개별 항목까지) ---")
for i in dictionary:
    if type(dictionary[i]) != list:
        print(f"{dictionary[i]}")
    else:
        for j in range(len(dictionary[i])):
            print(f"{dictionary[i][j]}")
print()