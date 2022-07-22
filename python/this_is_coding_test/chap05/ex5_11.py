from collections import deque

depth, width = map(int, input().split())

direction = [
    [-1, 0], [1, 0], [0, 1], [0, -1]
]

graph = []
for _ in range(depth):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for ix, iy in direction:
            nx = x + ix
            ny = y + iy
            if 0 <= nx < depth and 0 <= ny < width and graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))

    return graph[depth - 1][width - 1]


print(bfs(0, 0))