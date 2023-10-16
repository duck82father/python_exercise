# 1. 구의 부피와 겉넓이

rad = float(input("구의 반지름을 입력해주세요 : "))
pi = 3.141592
vol = (4/3)*pi*(rad**3)
surf = 4*pi*(rad**2)

result_vol = f'= 구의 부피는 {vol}입니다.'
result_surf = f'= 구의 겉넓이는 {surf}입니다.'

print(result_vol)
print(result_surf)


# 2. 피타고라스의 정리

sa = float(input("밑변의 길이를 입력해주세요: ")) 
sb = float(input("높이의 길이를 입력해주세요: ")) 
sc = (sa**2+sb**2)**(0.5)

result = "= 빗변의 길이는 {}입니다.".format(sc)

print(result)
