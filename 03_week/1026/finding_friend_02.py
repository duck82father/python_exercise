py_graph = {
    'A': ['B'],
    'B': ['A','C','J'],
    'C': ['B','F','D','G','I'],
    'D': ['C','E'],
    'E': ['D','K'],
    'F': ['C','H','I','O'],
    'G': ['C','K'],
    'H': ['F','N'],
    'I': ['C','F','K'],
    'J': ['B','M'],
    'K': ['I','G','E','L'],
    'L': ['K'],
    'M': ['N','J'],
    'N': ['M','H'],
    'O': ['F'],
}

start = input("찾을 친구를 입력하시오(A ~ O) : ").upper()
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
# friends = sorted(list(set(friends)))
friends = [friend for friend in sorted(list(set(friends))) if friend != start]

print("{}의 {}촌수의 친구는 {}입니다.".format(start, count, friends))