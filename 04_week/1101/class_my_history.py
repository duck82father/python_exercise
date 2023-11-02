# 클래스는 속성, 매서드만 갖는다.

# 생성자로 관리
class His:
    def __init__(self):
        self.entries = []

    def add_entry(self, a, b, operation, result):
        entry = f"{a}{operation}{b}={result}"
        self.entries.append(entry)
        return self.entries

class Calc:
    # def __init__(self) -> None:
    #     pass

    # 함수의 형태를 띄고 있지만, 클래스안에 있을 때는 '매서드'라고 표현한다.
    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    def mul(a,b):
        return a*b

    def div(a,b):
        if b == 0:
            return "0은 분모사용불가"
        return a*b

his = His()
cal1 = Calc
cal2 = Calc

r1 = cal1.add(1, 2)
print(his.add_entry(1, 2, '+', r1))

r2 = cal2.add(3, 4)
print(his.add_entry(3, 4, '+', r2))