# <코드>
# friend_bfs.py

def bfs(graph, start, max_depth):
    # 방문한 노드를 저장할 집합
    visited = set()
    # 탐색할 노드와 현재 깊이(촌수)를 저장하는 큐
    queue = [(start, 0)]
    # 관련된 사람들과 그들과의 촌수를 저장할 리스트
    related_people = []

    while queue:  # 큐에 탐색할 노드가 남아있다면 반복
        person, depth = queue.pop(0)  # 큐의 첫 번째 노드와 그 노드의 깊이(촌수)를 가져옴
        
        # 탐색 깊이가 주어진 최대 촌수 이내이고 시작 노드가 아니면 결과 리스트에 추가
        if depth <= max_depth and person != start:
            related_people.append((person, depth))
        
        # 현재 노드를 아직 방문하지 않았다면
        if person not in visited:
            visited.add(person)  # 방문 목록에 추가

            # 이웃 노드들을 탐색 목록(큐)에 추가
            for neighbor in graph.get(person, []):
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))

    return related_people  # 결과 리스트 반환

def main():
    # 사용자에게 가능한 모든 사람 목록을 보여줌
    print("가능한 사람들:", ", ".join(py_graph.keys()))

    # 사용자에게 자신의 이름을 입력받음
    person = input("자신의 이름을 입력하세요: ").upper()
    
    # 입력받은 이름이 그래프에 없다면 메시지 출력
    if person not in py_graph:
        print(f"{person}은/는 그래프에 없습니다.")
        return

    # 사용자에게 찾고 싶은 촌수를 입력받음
    depth = int(input(f"몇 촌 이내의 친척을 찾고 싶은지 입력하세요 (예: 1촌, 2촌 등): "))

    # BFS 함수를 사용하여 관련된 사람들을 찾음
    related_people = bfs(py_graph, person, depth)
    # 결과를 출력
    print(f"{person}의 {depth}촌 이내 친척들:")
    for p, d in related_people:
        print(f"{p} ({d}촌)")

# 사람들과 그들의 관계를 나타내는 그래프
py_graph = {
    'A': ['B'],
    'B': ['A','C','D','I'],
    'C': ['B','D','E'],
    'D': ['B','C','F'],
    'E': ['C','F','G'],
    'F': ['D','E','G','H'],
    'G': ['E','F'],
    'H': ['F'],
    'I': ['B']
}

# 프로그램 시작
if __name__ == "__main__":
    main()

# =====
# 가능한 사람들: A, B, C, D, E, F, G,H,I
# 자신의 이름을 입력하세요: B
# 몇 촌 이내의 친척을 찾고 싶은지 입력하세요 (예: 1촌, 2촌 등): 2
# B의 2촌 이내 친척들:
# A (1촌)
# C (1촌)
# D (1촌)
# I (1촌)
# D (2촌)
# E (2촌)
# F (2촌)
