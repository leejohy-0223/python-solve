import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 수 입력
n, m = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담기 위한 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 최단 경로 테이블
distance = [INF] * (n + 1)

# 모든 간선 입력
for _ in range(m):
    n1, n2, tmp = map(int, input().split())
    graph[n1].append([n2, tmp])

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))  # 거리, 노드번호 순으로 넣기
    distance[start] = 0

    while q:
        dist, cur_node = heapq.heappop(q)

        #  여기에서 뽑아진 dist는 start에서 cur_node까지의 거리를 의미한다. 주석처리해도 될거같은뎉?
        if distance[cur_node] < dist:
            continue

        # 뽑아진 노드와 연결된 노드들 체크
        for next_node, next_dist in graph[cur_node]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra()

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])