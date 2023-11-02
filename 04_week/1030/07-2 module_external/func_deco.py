# 함수 데코레이터 생성
def test(function):
    
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    
    return wrapper  

@test
def hello():
    print("hello")


# 함수 호출
hello()