nums_lst = [[1,2,3,],[4,5],[7,8,9]]
print("변경 전 :", nums_lst)

# 요소 추가
nums_lst.append([10,11,12])
nums_lst[1].insert(2,6)
nums_lst.extend([['a','b'],['c','d']])

print("변경 후 :", nums_lst)
