# 데이터 출력
flowers = [
    [5.1,3.5,'세토사'],[4.9,3,'세토사'],[6,3,'베르시컬러'],
    [6.2,2.8,'베르시컬러'],[5.5,2.3,'베르시컬러'],
    [6.3,3.3,'세토사'],[5.8,2.7,'베르시컬러'],[6.7,3,'세토사']
]

print("\n[ 꽃 데이터 (꽃받침의 길이, 꽃받침의 너비) ]")
for i in flowers:
    print(i)
print()

# 정보 입력 (x, y좌표)
x = float((input("x 좌표를 입력하시오(소수점 1자리) > ")))
y = float((input("y 좌표를 입력하시오(소수점 1자리) > ")))
xy = [x, y]

# 변수 선언
fw_sort = 0
fw_list = []
vector_list = []

# fw_list : 데이터와 입력된 좌표 사이의 vector값( vector_list )과 '세토나' 항목 참/거짓 여부 판단( fw_sort )하여 리스트로 정리
for fw in flowers:
    vector = ((fw[0]-xy[0])**2 + (fw[1]-xy[1])**2) ** 1/2
    vector_list.append(vector)
    if fw[2] == '세토사':
        fw_sort = 1
        fw_list.append((vector, fw_sort))
    else:
        fw_sort = 0

# vector 값을 오름차순으로 정리 (가까운 값부터)
vector_list = sorted(vector_list, key=float)

# 오름차순된 리스트에서 입력된 k번째의 항목을 기준으로 fw_list와 비교하여 작거나 같을 경우의 '세토나'의 수( sts )를 구함
k = int(input("k 값을 입력하시오 > "))
sts = 0
for i in fw_list:
    if i[0] <= vector_list[k-1]:
        sts += i[1]

# 결과값 출력
print("\n[ 결과값 ]")
print("k = {}일때, 세토사 : {}개, 베르시컬러 : {}개".format(k,sts,(k-sts)))

if k-sts > sts:
    print("\n입력된 좌표는 '베르시컬러'입니다.")
else:
    print("\n입력된 좌표는 '세토사'입니다.")