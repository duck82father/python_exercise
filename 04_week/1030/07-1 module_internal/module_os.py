import os

print("현재 운영체제: ", os.name)
print("현재 폴더 ", os.getcwd())    # current working directory
print("현재 폴더 내부요소: ", os.listdir())

os.mkdir("hello")   # MaKe directory
os.rmdir("hello")   # ReMove directory

with open("original.txt", 'w') as file:
    file.write("hello")

os.rename("original.txt", 'new.txt')

os.remove("new.txt") # os.unlink("new.txt")

os.system("dir")



