n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# chk 초기화
chk = [[0] * m for _ in range(n)]
chk[x][y] = 1

# 공간 데이터 입력
arr = [list(map(int, input().split())) for _ in range(n)]

# 북(0), 동(1), 남(2), 서(3)
go = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


def rotate():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


result = 1
while True:
    # 회전 먼저 수행
    rotate_count = 0
    going_chk = False
    while rotate_count != 4:
        rotate()
        rotate_count += 1

        nx = x + go[direction][0]
        ny = y + go[direction][1]

        # 해당 위치 가능 여부 체크
        if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] == 0 and arr[nx][ny] == 0:
            chk[nx][ny] = 1
            result += 1
            x, y = nx, ny
            going_chk = True
            break

    # 그 방향으로 가지 못했다면
    if not going_chk:
        # 한 칸 뒤로 가기
        x -= go[direction][0]
        y -= go[direction][1]

        # 뒤가 바다라면 끝
        if arr[x][y] == 1:
            break

print(result)
