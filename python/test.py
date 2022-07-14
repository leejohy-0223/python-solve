arr = [list(map(int, input().split())) for _ in range(10)]

x, y = 1, 1

while True:

    if arr[x][y] == 1:
        break

    if arr[x][y] == 0:
        arr[x][y] = 9
        if arr[x][y + 1] == 1:
            x += 1
        else:
            y += 1
    
    if arr[x][y] == 2:
        arr[x][y] = 9
        break

for i in arr:
    for j in i:
        print(j, end=" ")
    print()