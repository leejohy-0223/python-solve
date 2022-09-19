def solution(n, s, a, b, fares):
    INF = 200000001
    board = [[INF] * (n + 1) for _ in range(n + 1)]

    for n1, n2, dist in fares:
        board[n1][n2] = dist
        board[n2][n1] = dist

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]


    # 처음부터 따로가는 요금
    separateFee = board[s][a] + board[s][b]

    # 특점 지점 거칠 때 최저 요금
    minFee = INF
    for i in range(1, n + 1):
        if i == s:
            continue
        tmpFee = board[s][i]
        tmpFee += board[i][a] if i != a else 0
        tmpFee += board[i][b] if i != b else 0

        minFee = min(minFee, tmpFee)

    return min(separateFee, minFee)


if __name__ == '__main__':
    # print(solution(6, 4, 6, 2,
    #                [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
    #                 [1, 6, 25]]))
    print(solution(6, 4, 5, 6,
                   [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
