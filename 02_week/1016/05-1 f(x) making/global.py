c=0

# c는 scope.... 뭐라고 해야하나
def my_fn(a, b):
   c=a+b
   return c

# 참조 (global) 지정
def my_fn(a, b):
   global c
   c=a+b
   return c

print(my_fn(1,2))
print(c)