import sys

def solution(N, road, K):
    answer = 0
    INF = sys.maxsize
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    dist[1][1] = 0
    for n1, n2, d in road:
        dist[n1][n2] = min(d, dist[n1][n2])
        dist[n2][n1] = min(d, dist[n2][n1])

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(1, N + 1):
        if dist[1][i] <= K:
            answer += 1

    return answer


if __name__ == '__main__':
    # print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
    # print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	, 4))
    print(solution(1, [[]], 4))
