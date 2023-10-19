# csv 출력 함수

def write_file(text):
    with open('.\\02_week\\1018\\csv_test\\output.csv', 'w', encoding='utf-8') as file:
        file.write(text)
    print(text)