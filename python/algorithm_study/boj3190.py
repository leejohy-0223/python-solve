from sys import stdin
from collections import deque

# empty : 0 ,snake = 1, apple : 2
# 북(0), 동(1), 남(2), 서(3)
dir_array = [
    [-1, 0], [0, 1], [1, 0], [0, -1]
]

arr_size = int(stdin.readline())

board = [[0] * arr_size for _ in range(arr_size)]

snake_body = deque([[0, 0]])
apple_count = int(stdin.readline())

for _ in range(apple_count):
    x, y = map(int, stdin.readline().split())
    board[x - 1][y - 1] = 2

command_count = int(stdin.readline())
command = dict()
for _ in range(command_count):
    split = stdin.readline().split()
    x, direction = int(split[0]), split[1]
    command[x] = direction

# move
go, time = 1, 0

while True:
    #  시간 올리기
    time += 1

    nx = snake_body[0][0] + dir_array[go][0]
    ny = snake_body[0][1] + dir_array[go][1]

    # 진입 조건
    if 0 <= nx <= arr_size - 1 and 0 <= ny <= arr_size - 1:
        # 몸과 충돌나면 끝내기
        if [nx, ny] in snake_body:
            print(time)
            break

        # 머리 먼저 움직이고,
        snake_body.appendleft([nx, ny])

        # 사과가 있으면 꼬리 자르지 말기
        if board[nx][ny] == 2:
            board[nx][ny] = 0
        else:
            snake_body.pop()

    # 벽을 만났다면 끝내기
    else:
        print(time)
        break

    #  방향 전환이 있으면 바꾸기
    if time in command:
        if command.get(time) == 'D':
            go += 1
            if go == 4:
                go = 0
        else:
            go -= 1
            if go == -1:
                go = 3
