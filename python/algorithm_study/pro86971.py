# wire 하나를 끊고 1번 기준으로 DFS해서 count 계산
count = 100
tmp = 0


def solution(n, wires):
    global tmp
    global count
    map_route = dict()

    for i in range(0, n + 1):
        map_route[i] = []

    for wire in wires:
        x, y = wire[0], wire[1]
        map_route[x].append(y)
        map_route[y].append(x)

    for wire in wires:
        x, y = wire[0], wire[1]
        # 양방향 끊고
        map_route[x].remove(y)
        map_route[y].remove(x)

        # DFS
        visited = [False for _ in range(n + 1)]
        tmp = 0
        DFS(1, map_route, visited)

        count = min(count, abs(tmp - (n - tmp)))

        # 다시 연결
        map_route[x].append(y)
        map_route[y].append(x)

    return count


def DFS(now, map_route, visited):
    global tmp
    # 현 노드 방문 처리
    visited[now] = True
    tmp += 1

    for i in map_route[now]:
        if not visited[i]:
            DFS(i, map_route, visited)


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
