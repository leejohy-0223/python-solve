import sys

def solution(N, road, K):
    INF = sys.maxsize
    dists = [INF] * (N + 1)
    dists[1] = 0
    q = [1]

    while q:
        cur = q.pop(0)
        for n1, n2, d in road:
            if n1 == cur or n2 == cur:
                target = n2 if n1 == cur else n1
                if dists[target] > dists[cur] + d:
                    dists[target] = dists[cur] + d
                    q.append(target)

    return sum(1 for i in dists if i <= K)


if __name__ == '__main__':
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
    # print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	, 4))
    # print(solution(1, [[]], 4))
