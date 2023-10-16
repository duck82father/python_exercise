# 변수 선언
score = float(input("학점 입력 > "))

if score == 4.5 :
    print("A+")
elif 4.0 <= score :
    print("A")
elif 3.5 <= score :
    print("B")
elif 3.0 <= score :
    print("C")
elif 2.5 <= score :
    print("D")
else :
    print("F")


# 강제 에러 구문 'raise NotImplementedError'