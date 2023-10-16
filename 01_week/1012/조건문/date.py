# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print(now)

# 오전 구분
if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))

# 오후 구분
if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour))

# 계절 구분
if now.month <= 5 or now.month == 12 :
    print("이번 달은 {}월로 봄입니다.".format(now.month))
elif now.month <= 8 :
    print("이번 달은 {}월로 여름입니다.".format(now.month))
elif now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
else :
    print("이번 달은 {}월로 겨울입니다.".format(now.month))


