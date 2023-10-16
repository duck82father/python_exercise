###
# 입력데이터가 바뀌어도 공항명과 주차수를 추출하기
###

add2 = '청주,120390,"21(일반13,소형8)",164404,5267'
print(add2)

add3 = '포항경주,32617,"5(일반5,소형0)",17327,452'
print(add3)

print()

lst2 = add2.split(",")
print(lst2)
sta = lst2[2].find("(")
lst2_txt = "{}, {}".format(lst2[0],lst2[2][1:sta])
print(lst2_txt)

print()

lst3 = add3.split(",")
print(lst3)
sta = lst3[2].find("(")
lst3_txt = "{}, {}".format(lst3[0],lst3[2][1:sta])
print(lst3_txt)
