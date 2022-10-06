import sys

input = sys.stdin.readline
INF = int(1e9)


def bf():
    # 시작 노드 초기화
    distance[1] = 0

    # 전체 n번 반복
    for i in range(n):

        # 모든 road 검사
        for cur_node, next_node, cost in roads:
            if distance[next_node] > cost + distance[cur_node]:
                distance[next_node] = cost + distance[cur_node]

                # n번 반복 됐을 때(n - 1이면 n번 반복됨) 갱신된거라면 음의 사이클 형성을 의미
                if i == n - 1:
                    return True

    return False


tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    roads = []
    distance = [INF] * (n + 1)

    # 도로 가져오기
    for _ in range(m):
        s, e, t = map(int, input().split())
        roads.append((s, e, t))
        roads.append((e, s, t))

    # 웜홀 가져오기
    for _ in range(w):
        s, e, t = map(int, input().split())
        roads.append((s, e, -t))

    print("NO" if not bf() else "YES")