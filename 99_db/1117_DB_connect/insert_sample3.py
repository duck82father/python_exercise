from DBConnector import MariaDBConnector
import DBConnector

import insert_dummy

dummy_data = insert_dummy.make_dummy(5000, 1000)
students_data = dummy_data['students']
grades_data = dummy_data['grades']

batch_size = 20

config = DBConnector.config

db = MariaDBConnector(config)
conn = db.connect()
cur = conn.cursor()

for i in range(0, len(students_data), batch_size):
    batch = students_data[i:i+batch_size]
    print(batch)
    # cur.executemany("INSERT INTO students (id, `name`, birthdate, gender) VALUES (%s,%s,%s,%s);", batch)
    # conn.commit()

# for i in range(0, len(grades_data), batch_size):
#     batch = grades_data[i:i+batch_size]
    # cur.executemany("INSERT INTO grades (student_id, course, grade) VALUES (%s,%s,%s);", batch)
    # conn.commit()

db.close()