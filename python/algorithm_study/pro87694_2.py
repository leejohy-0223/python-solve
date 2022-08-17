from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 51 for _ in range(51)]
    cX = characterX
    cY = characterY
    iX = itemX
    iY = itemY
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[False] * 51 for _ in range(51)]

    # 내부 채우기
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                board[i][j] = 1

    # 내부 지우기
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 + 1, y2):
            for j in range(x1 + 1, x2):
                board[i][j] = 0

    # 캐릭터 위치 넣기
    visited[cY][cX] = True
    q = deque([(cX, cY)])
    while q:
        nX, nY = q.popleft()
        if nX == iX and nY == iY:
            return board[nY][nX] - 1

        for i in range(4):
            pX = nX + d[i][0]
            pY = nY + d[i][1]

            if board[pY][pX] != 0 and not visited[pY][pX]:
                visited[pY][pX] = True
                board[pY][pX] = board[nY][nX] + 1
                q.append((pX, pY))


if __name__ == '__main__':
    # print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
