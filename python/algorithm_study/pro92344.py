# 1차원일 경우
# [1, 2, 4, 8, 9] -> 0 ~ 3까지 -2를 하고싶은 상황
# [-2, 0, 0, 0, 2]를 저장 .. 이런 방식으로 skill을 누적

# 2차원은
# [n 0 0 0 -n]
# [0 0 0 0 0]
# [0 0 0 0 0]
# [0 0 0 0 0]
# [-n 0 0 0 n]
# 마지막으로 새로운 배열에 대해 2차원 누적합 진행
n, m = 0, 0

def solution(board, skill):
    global n, m
    n, m = len(board), len(board[0])
    tmpBoard = [[0] * (m + 1) for _ in range(n + 1)]

    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            put_value(r1, r2, c1, c2, -degree, tmpBoard)
        else:
            put_value(r1, r2, c1, c2, degree, tmpBoard)

    # tmpBoard 누적합
    # 위 -> 아래
    for j in range(m + 1):
        for i in range(1, n + 1):
            tmpBoard[i][j] += tmpBoard[i - 1][j]

    # 왼 -> 오
    for i in range(n + 1):
        for j in range(1, m + 1):
            tmpBoard[i][j] += tmpBoard[i][j - 1]

    # 기존 보드와 합치기
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + tmpBoard[i][j] >= 1:
                answer += 1

    return answer


def put_value(r1, r2, c1, c2, degree, tmpBoard):
    # (r1, r2), (r2 + 1, c2 + 1) = degree 더하기
    tmpBoard[r1][c1] += degree
    if r2 + 1 < n + 1 and c2 + 1 < m + 1:
        tmpBoard[r2 + 1][c2 + 1] += degree

    # (r1, c2 + 1), (r2 + 1, c1) = degree 빼기
    if c2 + 1 < m + 1:
        tmpBoard[r1][c2 + 1] -= degree
    if r2 + 1 < n + 1:
        tmpBoard[r2 + 1][c1] -= degree


if __name__ == '__main__':
    print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

    # print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
