def solution(rows, columns, queries):
    answer = []

    board = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]

    for query in queries:
        x1, y1, x2, y2 = query
        last = board[x2][y2]
        minValue = last

        # 아래방향
        for i in range(x2, x1, -1):
            board[i][y2] = board[i - 1][y2]
            minValue = min(minValue, board[i][y2])

        # 오른쪽 방향
        for i in range(y2, y1, -1):
            board[x1][i] = board[x1][i - 1]
            minValue = min(minValue, board[x1][i])

        # 위 방향
        for i in range(x1 + 1, x2 + 1):
            board[i - 1][y1] = board[i][y1]
            minValue = min(minValue, board[i - 1][y1])

        # 왼쪽 방향
        for i in range(y1 + 1, y2):
            board[x2][i - 1] = board[x2][i]
            minValue = min(minValue, board[x2][i - 1])

        # 마지막 위치에 넣기
        board[x2][y2 - 1] = last

        answer.append(minValue)

    return answer


if __name__ == '__main__':
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    # print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    # print(solution(100, 97, [[1, 1, 100, 97]]))
