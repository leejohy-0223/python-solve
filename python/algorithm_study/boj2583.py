import sys

sys.setrecursionlimit(10**6)

# m : 세로, n : 가로
m, n, k = map(int, input().split())

board = [[0] * n for _ in range(m)]

# x가 가로, y가 세로임에 유의
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

# 하얀 공간 크기 넣기
answer = []

chk = [[False] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0


def dfs(y, x):
    global count
    for r in range(4):
        nx = dx[r] + x
        ny = dy[r] + y
        if 0 <= nx < n and 0 <= ny < m and not chk[ny][nx] and board[ny][nx] == 0:
            chk[ny][nx] = True
            count += 1
            dfs(ny, nx)


for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and not chk[i][j]:
            chk[i][j] = True
            count = 1
            dfs(i, j)
            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i, end=" ")
