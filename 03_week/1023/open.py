# --- open(), close() 함수 사용 ---

# 파일 열기
file = open(".\\basic.txt", "w")

# 파일에 텍스트 쓰기
file.write("Hello Python Programing...!")

# 파일 닫기
file.close()


# --- with as 문으로 변경 ---

# 파일 열기
with open('.\\basic_with.txt', 'w') as file:
    # 파일에 텍스트를 씁니다
    file.write("with ** as, open(), close(), .write(), .read()")

