import csv

# 함수 선언 : csv파일을 불러드려 내용을 출력 및 리턴
def csv_read(csv_file):
    data = csv.reader(open(csv_file, mode='r'))
    
    lst = []
    for row in data:
        print(row)
        lst += row

    sum = 0
    for i in lst:
        print(i)
        i = int(i)
        sum += i

    print("[ csv 파일 계산결과 ]")
    print("csv 파일 개별 항목 :", lst, type(lst))
    print("csv 개별 항목의 합 :", sum, type(sum))
    print()
    
    return lst, sum
    

# 자체파일 실행일 경우 예시 csv 문서를 들러들인 후 출력
if __name__ == '__main__':
    import os
    csv_test = os.getcwd() + "\\02_week\\1018\\csv_test\\example.csv"
    csv_read(csv_test)