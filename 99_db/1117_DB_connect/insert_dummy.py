import random
from datetime import datetime, timedelta

def random_set(x=100, n=50):
    # 1부터 n까지의 숫자 중에서 중복되지 않는 m개의 숫자를 무작위로 선택
    return random.sample(range(1, x+1), n)

def make_dummy(x, n):
    # 점수 옵션
    GRADES = ('A', 'B', 'C')

    dummy_data = {'students':[], 'grades':[]}
    id_list = random_set(x, n)

    sn = 0    
    for i in range(len(id_list)):
        sn = sn + 1
        # 학생정보
        name = f'학생{id_list[i]}'
        year = random.randint(1990, 2020)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birthdate = datetime(year, month, day).strftime('%Y-%m-%d')
        gender = random.choice(['Male', 'Female', 'Other'])
        dummy_data['students'].append((sn,name,birthdate,gender))
        # print(f"INSERT INTO students (id, `name`, birthdate, gender) VALUES ({i}, {name}, '{birthdate}', '{gender}');")
        # 학생점수
        for subject in ['국어', '영어', '수학']:
            # 랜덤 점수 선택
            grade = random.choice(GRADES)
            dummy_data['grades'].append((sn,subject,grade))
            # insert문 생성
            # print(f"INSERT INTO geades (student_id, course, grade) VALUES ({i}, '{subject}', '{grade}');")
    return dummy_data

if __name__ == "__main__":
    # 더미 데이터 생성 제한
    MAX = 100  # 상한값
    MIN = 50   # 선택할 숫자의 개수
    BATCH_SIZE = 10

    print(make_dummy(MAX, MIN))