from test_read import csv_read
from test_write import write_file
import os

# 입력할 파일 위치 및 파일명
csv_test = os.getcwd() + "\\02_week\\1018\\csv_test\\example.csv"

# 읽기 함수에 적용
sum = csv_read(csv_test)

# 읽기 함수에서 return된 값을 쓰기 함수에 적용
text_sum = "output.csv 파일에 출력된 값 > \'sum = {}\'".format(sum)
write_file(text_sum)