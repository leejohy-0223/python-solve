from collections import deque

# BFS 정의
def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# 각 노드 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드 방문 정보를 초기화
visited = [False] * 9

# BFS 호출
bfs(graph, 1, visited)