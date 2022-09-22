def solution(c, r, k):
    if c * r < k:
        return 0

    board = [[0] * c for _ in range(r)]
    value = 1
    sx, sy = 0, 0
    while c >= 0 and r >= 0:
        # 아래 방향
        for y in range(sy, sy + r):
            board[y][sx] = value
            if value == k:
                return sx + 1, y + 1
            value += 1

        # 왼쪽 방향
        for x in range(sx + 1, sx + c):
            board[sy + r - 1][x] = value
            if value == k:
                return x + 1, sy + r
            value += 1

        # 위 방향
        for y in range(sy + r - 2, sy - 1, -1):
            board[y][sx + c - 1] = value
            if value == k:
                return sx + c, y + 1
            value += 1

        # 오른쪽 방향
        for x in range(sx + c - 2, sx, -1):
            board[sy][x] = value
            if value == k:
                return x + 1, sy + 1
            value += 1
        r -= 2
        c -= 2
        sx += 1
        sy += 1


if __name__ == '__main__':
    c1, r1 = map(int, input().split())
    k1 = int(input())
    result = solution(c1, r1, k1)
    if result == 0:
        print(0)
    else:
        print(result[0], result[1])