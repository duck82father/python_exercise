#import datetime

#now = datetime.datetime.now()

a = input("몇 월? >")
nowmonth = int(a)

if 3 <= nowmonth <= 5 :
    print("봄")
elif 6 <= nowmonth <=8 :
    print("여름")
elif 9 <= nowmonth <=11 :
    print("가을")
else :
    print("겨울")