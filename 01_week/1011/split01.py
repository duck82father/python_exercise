# 청주,120390,"21(일반13,소형8)",164404,5267
addr = "청주,120390,\"21(일반13,소형8)\",164404,5267"
txt = addr.split(",")

place = txt[0]
num = txt[2][1:3]
result = place+", "+num

print(result)

# 배열 테스트
txt2 = ["문자", "숫자", [1,2,3],"외계어"]
print(txt2[2][0])
print(type(txt2))

print(type(True))