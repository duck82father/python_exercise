from DBConnector import MariaDBConnector

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'admin',
    'password': '1234',
    'database': 'SampleSchool_test'
}

db = MariaDBConnector(config)

conn = db.connect()
cur = conn.cursor()
cur.execute("SELECT student_id, course_id from enrollments;")
datas = cur.fetchone()
conn.commit()

db.close()