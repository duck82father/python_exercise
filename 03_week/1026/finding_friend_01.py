py_graph = {
    'A': ['B'],
    'B': ['A','C','D'],
    'C': ['B','D','E'],
    'D': ['B','C','F'],
    'E': ['C','F','G'],
    'F': ['D','E','G'],
    'G': ['E','F']
}

start = input("찾을 친구를 입력하시오(A ~ G) : ").upper()
count = int(input("구할 촌수를 입력하시오 : "))
result = []


def finding_friend(start, count):
    global result
    result.extend(py_graph[start])
    if count > 1:
        for i in py_graph[start]:
            finding_friend(i, count-1)
    else:
        result.extend(py_graph[start])
    
    return result


friends = finding_friend(start,count)
friends = sorted(list(set(friends)))
print("{}의 {}촌수의 친구는 {}입니다.".format(start, count, friends))