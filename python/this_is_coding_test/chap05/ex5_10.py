# 상, 하, 좌, 우
direction = [
    [-1, 0], [1, 0], [0, 1], [0, -1]
]

depth = 0
width = 0


def solution(ice):
    global depth
    global width
    count = 0
    depth = len(ice)
    width = len(ice[0])

    for i in range(depth):
        for j in range(width):
            if ice[i][j] == 0:
                count += 1
                ice[i][j] = 1
                dfs(ice, i, j)

    return count


def dfs(arr, x, y):
    for i in range(4):
        nx = x + direction[i][0]
        ny = y + direction[i][1]
        if 0 <= nx < depth and 0 <= ny < width and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            dfs(arr, nx, ny)


if __name__ == '__main__':
    print(solution([[0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 1], [0, 0, 0, 0, 0]]))
