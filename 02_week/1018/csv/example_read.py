import csv

# 파일을 전달
def read_file(csv_file): 
    lst = []

    # 파일을 읽기모드(r)로 열고(open) file에 담는다.
    with open(csv_file, mode='r') as file:
    
        # csv 데이터 (list로 속성 변환??)
        csv_reader = csv.reader(file)

        # 읽은 파일의 각 행을 반복 가능한 객체로 저장한다.
        for row in csv_reader:
            lst += row
            # l += flatting_list.flatting(row)
    
    # print(type(csv_reader))
    print("본 모듈의 '__name__'값은", f"\'{__name__}\'")
    return lst

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# '__name__'이 '__main__' 이라면 python 파일을 직접 실행한 것
# 외부에서 이 python 파일을 실행할 경우 __name__ 값은 파일명인 'example_read'가 된다.

if __name__ == '__main__':
    import os

    current_dir = os.getcwd()
    csv_file = current_dir + '\\02_week\\1018\\csv\\example.csv'

    print(read_file(csv_file))