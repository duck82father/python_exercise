from datetime import datetime

nowtime = datetime.now()
print(nowtime)

print("시간을 포맷에 맞춰 출력하기\n")

output_a = nowtime.strftime("%Y.%m.%d %H:%M:%S")
print("a, ", output_a)

output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format("b, ", nowtime.year,nowtime.month,nowtime.day,nowtime.hour,nowtime.minute,nowtime.second)
print(output_b)

output_c = nowtime.strftime("%Y{} %m.%d %H:%M:%S")