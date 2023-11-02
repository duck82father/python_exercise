# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

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

# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 17, 18, 14, 43),
    Student("구지연", 34, 72, 61, 53),
    Student("나선주", 86, 48, 78, 12)
]

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student))



