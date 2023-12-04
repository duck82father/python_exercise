import random
import pandas as pd
from datetime import date

# students
# for i in range(1, 501):
#     birthdate = date(random.randrange(1990, 2010), random.randint(1, 12), random.randint(1, 28))  
#     gender = random.choice(['Male', 'Female', 'Other'])
#     print("insert into students (name, birthdate, gender) values (\"학생{:03}\", \"{}\", \"{}\");".format(i, birthdate, gender))

# # enrollments : 500명
# enrollments_all = "insert into enrollments (student_id, course_id, enrollment_date) values "
# for i in range(1, 501):
#     # random.choices(범위, k=갯수)는 중복 포함 선택
#     # random.choices(범위, k=갯수)는 중복 없이 선택
#     courses = random.sample(range(1,11), k=5)
#     date_range = pd.date_range(start="2022-01-01", end="2023-11-21")
#     enrollment_date = str(random.choice(date_range))
#     for course in sorted(courses):
#         enrollments_all += "(\"{}\", \"{}\", \"{}\"), ".format(i, course, enrollment_date[:10])
# enrollments_all = enrollments_all[:-2] + ";"
# print(enrollments_all)


# # enrollments : 학생 1 ~ 500중 랜덤하게 450명(중목X) / 1인당 5개 과목(랜덤)
# enrollments_all = "insert into enrollments (student_id, course_id, enrollment_date) values "

# random_range = random.sample(range(1,500), k=450)
# random_range = sorted(random_range)
# for i in random_range:
#     courses = random.sample(range(1,11), k=5)
#     date_range = pd.date_range(start="2022-01-01", end="2023-11-21")
#     enrollment_date = str(random.choice(date_range))
#     for course in sorted(courses):
#         enrollments_all += "(\"{}\", \"{}\", \"{}\"), ".format(i, course, enrollment_date[:10])
# enrollments_all = enrollments_all[:-2] + ";"

# print(enrollments_all)


# grades : 450명 중 1인당 3개 랜덤 과목의 점수 추가
all_grade = "insert into grades (enrollment_id, grade) values "
counts = 0

for i in range(1, 451):
    for j in random.sample(range(1, 6), k=5):
        if j > 2:
            counts += 1
            random_grade = random.choice(['A', 'B', 'C', 'F'])
            all_grade += "({}, \"{}\"), ".format(counts, random_grade)
        else:
            counts += 1
            all_grade += "({}, {}), ".format(counts, 'Null')
            continue

all_grade = all_grade[:-2] + ";"
print(all_grade)
