import heapq
import sys


def dijkstra(s, e):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for k in graph[now]:
            cost = d + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))

    return distance[e]

N, E = map(int, input().split(" "))
INF = sys.maxsize
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    n1, n2, dist = map(int, input().split(" "))
    graph[n1].append([n2, dist])
    graph[n2].append([n1, dist])

v1, v2 = map(int, input().split(" "))

answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

print(answer if answer < INF else -1)