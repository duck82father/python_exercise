from Calculator import Calculator

if __name__ == "__main__":
    # 사용자로부터 값을 입력받음
    a = float(input("첫 번째 숫자를 입력하세요: "))
    b = float(input("두 번째 숫자를 입력하세요: "))

    calc = Calculator()

    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.subtract(a, b)}")
    print(f"{a} x {b} = {calc.multiply(a, b)}")
    print(f"{a} / {b} = {calc.divide(a, b)}")
