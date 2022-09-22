## dfs를 이용한 접근 - 시간 초과

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

route = []
summit = set()
chk = []
answer = set()
gateInfo = set()
resultSummit = sys.maxsize
minIntensity = sys.maxsize
dp = []


def dfs(node, maxValue):
    global minIntensity
    if node in summit:
        if maxValue <= minIntensity:
            if maxValue < minIntensity:
                minIntensity = maxValue
                answer.clear()
            answer.add((node, minIntensity))
        return

    for nextNode, dist in route[node]:
        if not chk[nextNode] and nextNode not in gateInfo:
            if dist > minIntensity:
                continue
            if dp[nextNode] < maxValue:
                continue
            dp[nextNode] = maxValue
            tmpValue = max(maxValue, dist)
            chk[nextNode] = True
            dfs(nextNode, tmpValue)
            chk[nextNode] = False


def solution(n, paths, gates, summits):
    global route, summit, chk, gateInfo, dp
    summit = set(summits)
    gateInfo = set(gates)
    route = defaultdict(list)
    dp = [sys.maxsize] * (n + 1)

    for n1, n2, dist in paths:
        route[n1].append((n2, dist))
        route[n2].append((n1, dist))

    for gate in gates:
        chk = [False] * (n + 1)
        chk[gate] = True
        dfs(gate, 0)

    return list(sorted(answer, key=lambda r: r[0])[0])


if __name__ == '__main__':
    print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
                   [1, 3], [5]))

    # print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    #                [1], [2, 3, 4]))

    # print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    #                [3, 7], [1, 5]))

    # print(solution(3, [[1, 2, 4], [1, 3, 4]], [1], [2, 3]))
