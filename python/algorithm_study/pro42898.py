def solution(m, n, puddles):
    board = [[10001] * (m + 1) for _ in range(n + 1)]
    dp = [[1000000007] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 0
    dp[1][1] = 1

    for pubble in puddles:
        board[pubble[1]][pubble[0]] = 999999

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if board[i][j] != 999999:
                board[i][j] = min(board[i - 1][j], board[i][j - 1]) + 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if board[i][j] != 999999:
                if board[i - 1][j] == board[i][j - 1]:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
                else:
                    # 최소쪽의 거리를 전달해준다.
                    dp[i][j] = dp[i][j - 1] % 1000000007 if board[i - 1][j] > board[i][j - 1] else dp[i - 1][j] % 1000000007

    return dp[n][m]

if __name__ == '__main__':
    # print(solution(4, 3, [[2, 2]]))
    # print(solution(10, 10, [[2, 2], [3, 4], [3, 1], [4, 5], [2, 3]]))
    print(solution(2, 3, []))