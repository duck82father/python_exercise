from DBConnector import MariaDBConnector

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'admin',
    'password': '1234',
    'database': 'SampleSchool'
}

db = MariaDBConnector(config)

conn = db.connect()
cur = conn.cursor()
cur.execute("INSERT INTO students (name, birthdate, gender) VALUES ('학생43', '2000-04-20', 'Male');")
conn.commit()

db.close()