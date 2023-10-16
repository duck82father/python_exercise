# 현재 시간 구하기

import time
from datetime import datetime

def twelve(a):
    if a.hour>12:
        return a.hour%12
    else:
        return a.hour

def time_data():
    now = datetime.now()
    twelve_hour=twelve(now)
    nt = f"{twelve_hour:02}{now.minute:02}{now.second:02}"
    print() 
    for n in [0,1,2,3,4]:
        print(
            bt[nt[0]][n],
            bt[nt[1]][n],
            bt[":"][n],
            bt[nt[2]][n],
            bt[nt[3]][n],
            bt[":"][n],
            bt[nt[4]][n],
            bt[nt[5]][n]
            )

bt={
    '0':[" ### ","#   #","#   #","#   #"," ### "],
    '1':["  #  "," ##  ","  #  ","  #  "," ### "],
    '2':[" ### ","#   #","   # ","  #  ","#####"],
    '3':[" ### ","#   #","  ## ","#   #"," ### "],
    '4':["   # ","  ## "," # # ","#####","   # "],
    '5':[" ####","#    ","#####","    #"," ### "],
    '6':[" ### ","#    ","#####","#   #"," ### "],
    '7':["#####","    #","   # ","  #  "," #   "],
    '8':[" ### ","#   #"," ### ","#   #"," ### "],
    '9':[" ### ","#   #"," ### ","  #  "," #   "],
    ":":["   "," # ","   "," # ","   "]
}

while True:
    time_data()
    time.sleep(1)