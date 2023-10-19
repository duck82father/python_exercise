# 파일 읽기 > 합산 > 파일 쓰기

# 모듈 불러오기
import os
import example_read
import example_write

# 파일 읽기
current_dir = os.getcwd()
csv_file = current_dir + '\\02_week\\1018\\csv\\example.csv'
list = example_read.read_file(csv_file)

# 합산
sum = 0
for i in list:
    if type(i) is str:
        i = int(i)
    sum += i

print(list, "의 합은", sum)

# 파일 쓰기
text = "sum: {}".format(sum)
example_write.write_file(text)