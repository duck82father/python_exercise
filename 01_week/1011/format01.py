# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{2}, {1}, {0}".format(3000,4000,5000)
format_d = "{} + {} + {}".format(1,"문자열",True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

cc = format_c.split(", ")
print(cc[0], cc[2])

# 빈칸
print()

# f"{}" 함수로 변경
n1 = input("n1를 입력하시오 > ")
n2 = input("n2를 입력하시오 > ")
n3 = input("n3를 입력하시오 > ")

format_a = f"{n1}만 원"
format_b = f"파이썬 열공하여 첫 연봉 {n1}만 원 만들기"
format_c = f"{n1}, {n2}, {n3}"
format_d = f"{1} + {"문자열"} + {True}"

print(format_a)
print(format_b)
print(format_c)
print(format_d)

cc = format_c.split(", ")
print(cc[0], cc[2])