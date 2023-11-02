from random import randint

# 속성, 매서드
# ApplePie, Apple 


class Calculator1:
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



if __name__ == "__main__":
    # 사용자로부터 값을 받음
    a = randint(1, 100)
    b = randint(1, 100)
    print("a = {}, b = {}".format(a, b))
    print(Calculator.add(a,b))


# class calc():
#     def __init__(self, int_a, int_b):
#         self.int_a = int_a
#         self.int_b = int_b
#         pass

#     def get_add(self):
#         result = self.int_a + self.int_b
#         return result
    
#     def get_sub(self):
#         result = self.int_a - self.int_b
#         return result

#     def get_mul(self):
#         result = self.int_a * self.int_b
#         return result

#     def get_div(self):
#         if self.int_b == 0:
#             result = "0으로 나눌 수 없습니다."
#         else:
#             result = self.int_a / self.int_b
#         return result

#     def get_sum(self):
#         result = self.int_a + self.int_b
#         return result
    
#     def get_avrg(self):
#         result = self.get_sum() / 2
#         return result

# result = calc(1,2).get_avrg()
# print(result)

# result = calc(1,0).get_div()
# print(result)