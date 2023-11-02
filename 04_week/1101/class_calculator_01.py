# 내 계산기
# + - * /

class Calc:
    def __init__(self, int_a, int_b):
        self.int_a = int_a
        self.int_b = int_b
        pass

    def get_add(self):
        result = self.int_a + self.int_b
        return result
    
    def get_sub(self):
        result = self.int_a - self.int_b
        return result

    def get_mul(self):
        result = self.int_a * self.int_b
        return result

    def get_div(self):
        if self.int_b == 0:
            return "0으로 나눌 수 없습니다."
        else:
            result = self.int_a / self.int_b
        return result

    def get_sum(self):
        result = self.int_a + self.int_b
        return result
    
    def get_avrg(self):
        result = self.get_sum() / 2
        return result

result = Calc(1,2).get_avrg()
print(result)

result = Calc(1,0).get_div()
print(result)