# ?????????????????????????????????

# 모듈 가져오기
from functools import wraps

def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        print("인사가 시작되었습니다.")
        function(*arg, **kwargs)
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

# 함수 호출
hello()