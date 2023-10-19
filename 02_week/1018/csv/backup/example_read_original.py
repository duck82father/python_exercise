import csv  # csv 읽기함수?
import os   # os(visual studio code)?

#

# 함수 선언
def getSum(list):
    sum = 0
    for i in list:
        i = int(i)
        print("i 순환 {} {}".format(i, type(i)))
        sum += i
    print("합은 {}".format(sum))

#

current_dir = os.getcwd()
print(current_dir)
# 경로를 구분할 때 \\를 사용
csv_file = current_dir + '\\02_week\\1018\\csv\\example.csv'

# 파일을 읽기모드(r)로 열고(open) file에 담는다.
with open(csv_file, mode='r') as file:
    
    # csv 데이터를 list로 속성 변환한다.
    csv_reader = list(csv.reader(file))

    # 읽은 파일의 각 행을 반복 가능한 객체로 저장한다.
    for row in csv_reader:
        print(row)

    # 1번 행의 값을 int로 불러 합계를 출력한다.
    output = 0
    for row_a in csv_reader[0]:
        i = int(row_a)
        output += i
    print(output)
    print()

getSum(csv_reader[0])



