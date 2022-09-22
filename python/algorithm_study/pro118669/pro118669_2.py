## heapq & dp를 이용한 방법
import sys
import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    route = defaultdict(list)
    INF = sys.maxsize
    intenseInfo = [INF] * (n + 1)

    gates = set(gates)
    summits = set(summits)

    checkHeap = []

    for n1, n2, dist in paths:
        route[n1].append((n2, dist))
        route[n2].append((n1, dist))

    # set the gate intense to zero. 가장 먼저 탐색되도록 지정한다.
    for gate in gates:
        intenseInfo[gate] = 0
        heapq.heappush(checkHeap, (0, gate))

    while checkHeap:
        intense, node = heapq.heappop(checkHeap)

        if node in summits or intenseInfo[node] < intense:  # 같은 경우는 체크 필요하다. 그걸 의도하고 넣어줬으니까.
            continue

        for nextNode, dist in route[node]:
            tmpMaxIntense = max(dist, intense)
            if tmpMaxIntense >= intenseInfo[nextNode]:  # 여기에서 같은 경우는 pass해야 한다. 이미 intense가 동일하면 이중 체크가 된다.
                continue
            intenseInfo[nextNode] = tmpMaxIntense
            heapq.heappush(checkHeap, (tmpMaxIntense, nextNode))

    answer = []
    for summit in summits:
        answer.append([summit, intenseInfo[summit]])

    return sorted(answer, key=lambda a: (a[1], a[0]))[0]


if __name__ == '__main__':
    print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
                   [1, 3], [5]))

    # print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    #                [1], [2, 3, 4]))

    # print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    #                [3, 7], [1, 5]))

    # print(solution(3, [[1, 2, 4], [1, 3, 4]], [1], [2, 3]))
