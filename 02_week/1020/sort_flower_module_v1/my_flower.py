# 두 벡터의 거리(벡터)
def dis(a, b):
    d = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return d

# 두 벡터사이의 거리를 리스트로 반환 (a = data_list , b = target )
def dis_list(a, b):
    d_list = []
    for i in a:
        d = dis(i,b)
        d_list.append(d)
    return d_list

# 작은 값부터 정렬
def sort(lst):
    print()
    print("print(lst)", lst)
    print("print(enumerate(lst))", enumerate(lst))
    print("list(print(enumerate(lst)))", list(enumerate(lst)))
    print()
    sorted_lst = sorted(enumerate(lst), key=lambda x: x[1])
    # 정렬된 (인덱스, 값) 쌍을 다시 정렬된 순서대로 인덱스를 추출
    sorted_idx = [index for index, value in sorted_lst]
    return sorted_idx

if __name__ == '__main__':
    target = [3,4]

    data = [1,2]
    print(dis(data,target))

    data_list = [[1,2], [3,5], [1,3]]
    target_list = dis_list(data_list, target)
    print(target_list)

    idx = sort(target_list)
    print(idx)

    # 가장 가까운 벡터는
    print(data_list[idx[0]])