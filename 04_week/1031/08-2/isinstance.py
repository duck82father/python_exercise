# 학생 클래스를 선언합니다.
class Student:
    def study(self):
        print("공부합시다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

# 교실 내부의 객체 리스트를 생성
classroom = [Student(),Teacher(),Student(),Teacher(),Student()]

# 반복을 적용해서 적절한 함수를 호출하게 합니다.
for person in classroom:
    if isinstance(person, Student):
        person.study()
    else:
        person.teach()

