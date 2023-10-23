# 파일 열기
with open(".\\basic.txt", "r") as file:
   # 파일을 읽고 출력
   contents= file.read()

print(contents)