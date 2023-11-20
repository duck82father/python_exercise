import datetime
import random

sql = ""
for i in range(1, 101):
    name = f'학생{i}'
    birthdate = datetime.date(2000, random.randint(1, 12), random.randint(1, 28))
    gender = random.choice(['Male', 'Female', 'Alien'])
    student_query = f"INSERT INTO students (name, birthdate, gender) VALUES ('{name}', '{birthdate}', '{gender}');"
    sql += '\n'
    sql += student_query

for i in range(1, 101):
    student_id = i
    course = random.choice(['수학', '영어', '과학'])
    grade = random.choice(['A', 'B', 'C', 'D', 'F'])
    grade_query = f"INSERT INTO grades (student_id, course, grade) VALUES ({student_id}, '{course}', '{grade}');"
    sql += '\n'
    sql += grade_query

print(sql)
