def solution(n1, m1, board1):
    chk = [[False] * m1 for _ in range(n1)]

    for i in range(n1):
        for j in range(m1):
            if board1[i][j] == '*':
                chk[i][j] = True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = []

    for i in range(1, n1 - 1):
        for j in range(1, m1 - 1):
            if board1[i][j] == '*':
                size = 1
                while True:
                    for k in range(4):
                        nx = i + (dx[k] * size)
                        ny = j + (dy[k] * size)
                        if 0 <= nx < n1 and 0 <= ny < m1 and board1[nx][ny] == '*':
                            continue
                        else:
                            break
                    else:
                        chk[i][j] = False
                        for k in range(4):
                            nx = i + (dx[k] * size)
                            ny = j + (dy[k] * size)
                            chk[nx][ny] = False
                        answer.append((i + 1, j + 1, size))
                        size += 1
                        continue
                    break

    for i in range(n1):
        for j in range(m1):
            if chk[i][j]:
                return -1

    print(len(answer))
    for a in answer:
        print(*a)

    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    result = solution(n, m, board)

    if result is not None:
        print(result)
