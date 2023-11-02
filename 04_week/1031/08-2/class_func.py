# 클래스 선언
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
        print(">> 현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
    
# 학생리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 17, 18, 14, 43),
    Student("구지연", 34, 72, 61, 53),
    Student("나선주", 86, 48, 78, 12)
]

Student.print()