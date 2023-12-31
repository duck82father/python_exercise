# 계산 결과를 관리하는 클래스 추가

# History.py
class History:
    def __init__(self):
        self.entries = []

    def add_entry(self, a, b, operation, result):
        entry = f"{a} {operation} {b} = {result}"
        self.entries.append(entry)

    def display(self):
        for entry in self.entries:
            print(entry)
