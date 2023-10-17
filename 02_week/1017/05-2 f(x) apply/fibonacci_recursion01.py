def fibonacci(n):
    if n == 1 or n == 2 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# 함수 호출
print("finonacci(35): ", fibonacci(35))
    
    