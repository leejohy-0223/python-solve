def solution(rows, columns, queries):
    answer = []
    board = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]

    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        stack = []

        # 오른쪽
        for i in range(c1, c2 + 1):
            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            board[r1][i] = stack[-2]

        # 아래
        for j in range(r1 + 1, r2 + 1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        # 왼쪽
        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        # 위쪽
        for l in range(r2 - 1, r1 - 1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))

    return answer


if __name__ == '__main__':
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    # print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    # print(solution(100, 97, [[1, 1, 100, 97]]))
