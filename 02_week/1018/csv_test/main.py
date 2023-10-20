import test_read
import test_write
import os

# 입력할 파일 위치 및 파일명
# csv_test = os.getcwd() + "\\02_week\\1018\\csv_test\\example.csv"
csv_test = ".\example.csv"

# 읽기 함수에 적용
lst, sum = test_read.csv_read(csv_test)

# 읽기 함수에서 return된 값을 쓰기 함수에 적용
text_sum = "개별 = {}\n총합 = {}".format(lst, sum)
test_write.write_file(text_sum)