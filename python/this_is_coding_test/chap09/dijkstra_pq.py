import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b까지 비용 = c라는 의미
    graph[a].append([b, c])


def dijkstra():
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))  # 0(거리)가 우선순위 기준이 된다.
    distance[start] = 0

    while q:
        # 가장 최단거리에 있는 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 세로 나온 dist가 기존 distance[now]보다 크다는 건 이미 처리되었다는 의미이니 pass
        if distance[now] < dist:
            continue

        # 현재 노드와 인접된 노드를 확인
        for i in graph[now]:
            # dist(부모라고 하자) 거리 + i[1](방금 연결되어 꺼내진 자식까지 거리)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])

