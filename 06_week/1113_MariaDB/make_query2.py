import random
from datetime import date


for i in range(1, 31):
    birthdate = date(random.randrange(2000, 2010), random.randint(1, 12), random.randint(1, 28))
    gender = random.choice(['남', '여', '기타'])
    print(f"insert into students (name, birthdate, gender) values (\"학생{i}\", \"{birthdate}\", \"{gender}\")")

for i in range(1, 31):
    course = random.choice(['영어', '수학', '국어', '과학', '체육', '음악'])
    grade = random.choice(['A', 'B', 'C', 'D', 'F'])
    print(f"insert into students (student_id, course, grade) values (\"{i}\", \"{course}\", \"{grade}\")")