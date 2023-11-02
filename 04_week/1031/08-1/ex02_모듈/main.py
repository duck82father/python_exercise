from operations import add, subtract, multiply, divide

if __name__ == "__main__":
    # 사용자로부터 값을 입력받음
    a = float(input("첫 번째 숫자를 입력하세요: "))
    b = float(input("두 번째 숫자를 입력하세요: "))
    
    print(f"{a} + {b} = {add.add(a, b)}")
    print(f"{a} - {b} = {subtract.subtract(a, b)}")
    print(f"{a} x {b} = {multiply.multiply(a, b)}")
    print(f"{a} / {b} = {divide.divide(a, b)}")
