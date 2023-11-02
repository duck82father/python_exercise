from datetime import datetime

nowtime = datetime.now()
print(nowtime)

print("시간을 포맷에 맞춰 출력하기\n")

output_a = nowtime.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(nowtime.year,nowtime.month,nowtime.day,nowtime.hour,nowtime.minute,nowtime.second)
output_c = nowtime.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")

print("a, ", output_a)
print("b, ", output_b)
print("c, ", output_c)