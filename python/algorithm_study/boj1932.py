n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        tmp = 0
        if j - 1 < 0:
            tmp = arr[i - 1][j]
        elif j >= i:
            tmp = arr[i - 1][j - 1]
        else:
            tmp = max(arr[i - 1][j - 1], arr[i - 1][j])

        arr[i][j] += tmp

print(max(arr[n - 1]))
