from DBConnector import MariaDBConnector
import DBConnector
import os

def csv_to_list(csvfile):
    text = []
    for line in csvfile:
        if line[0] == 'Q':
            continue
        tupleline = ()
        line = line.strip()
        if "\"" in line:
            line = line.replace(',\",', '$')
            line = line.replace(',\"', '$')
            line = line.replace('\",', '$')
            line = line.replace('\"', '$')
            line = line.split('$')
        else: 
            line = line.split(',')
        print(line)
        line = (line[0], line[1], int(line[2]))
        text.append(line)
    return text

batch_size = 500

cwd = os.getcwd()
file = os.path.join(cwd, '99_db', '1204_MariaDB_csv', 'chatbot_data.csv')
csvfile = open(file, 'r', encoding='UTF8')
csvfile = csv_to_list(csvfile)

config = DBConnector.config
db = MariaDBConnector(config)
conn = db.connect()
cur = conn.cursor()

for i in range(0, len(csvfile), batch_size):
    batch = csvfile[i:i+batch_size]
    print(batch)
    cur.executemany("INSERT INTO ChatCsv (`Question`, `Answer`, `Label`) VALUES (%s,%s,%d);", batch)
    conn.commit()

db.close()