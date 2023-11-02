# 클래스 선언

class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 17, 18, 14, 43),
    Student("구지연", 34, 72, 61, 53),
    Student("나선주", 86, 48, 78, 12)
]

# 1차 출력합니다.
print(">> 현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))

# 2차 출력
print()
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 17, 18, 14, 43),
    Student("구지연", 34, 72, 61, 53),
    Student("나선주", 86, 48, 78, 12)
]
print(">> 현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))

# 3차 출력
print()
Student.count=0
print(">> 현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))
