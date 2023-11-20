from DBConnector import MariaDBConnector
import DBConnector

config = DBConnector.config

db = MariaDBConnector(config)
conn = db.connect()
cur = conn.cursor()
cur.execute("INSERT INTO students (name, birthdate, gender) VALUES ('학생43', '2000-04-20', 'Male');")
conn.commit()
db.close()