# 딕셔너리 리턴하는 함수 선언
def create_student(name, korean, math, english, science):
    return {
        'name':name,
        'korean':korean,
        'math':math,
        'english':english,
        'science':science
    }

# 학생을 처리하는 함수 선언
def student_get_sum(student):
    return student["korean"] + student["math"] +\
            + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )


# 학생 리스트 선언
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 17, 18, 14, 43),
    create_student("구지연", 34, 72, 61, 53),
    create_student("나선주", 86, 48, 78, 12)
]

# 학생을 한명씩 반복

print("이름", "총점", "평균", sep='\t')
for student in students:
    print(student_to_string(student))