def solution(m, n, puddles):
    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1

    for pubble in puddles:
        board[pubble[1]][pubble[0]] = 999999

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if board[i][j] == 999999:
                board[i][j] = 0
                continue
            board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007

    return board[n][m]

if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))
    # print(solution(10, 10, [[2, 2], [3, 4], [3, 1], [4, 5], [2, 3]]))
    # print(solution(2, 3, []))