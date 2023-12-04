from datetime import datetime, timedelta

sql = ""
create_date = datetime.now()

for i in range(1, 101):
    name = '테스트데이터입니다 {:03d}'.format(i)
    content = '내용 없음'
    create_date += timedelta(seconds=1)
    question_query = f"INSERT INTO question (subject, content, create_date) VALUES ('{name}', '{content}', '{create_date}');"
    sql += '\n'
    sql += question_query

print(sql)