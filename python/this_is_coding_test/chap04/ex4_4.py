# n : 세로, m : 가로
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

chk = [[0] * m for _ in range(n)]

# 전체 맵 입력
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

chk[x][y] = 1

# 북(0), 동(1), 남(2), 서(3)
go = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


def rotate():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
while True:
    rotation_count = 0
    go_chk = False
    while rotation_count != 4:
        rotation_count += 1
        rotate()
        nx = x + go[direction][0]
        ny = y + go[direction][1]

        if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] == 0 and array[nx][ny] == 0:
            chk[nx][ny] = 1
            count += 1
            go_chk = True
            x, y = nx, ny
            break

    if not go_chk:
        # 한 칸 뒤로 이동한다.
        x -= go[direction][0]
        y -= go[direction][1]
        if array[x][y] == 1:
            break

print(count)
for i in chk:
    print(i)
