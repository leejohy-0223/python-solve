N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

max_sum = 0
# 가로
for i in range(N):
    max_sum = max(max_sum, sum(arr[i]))

# 세로
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += arr[j][i]
    max_sum = max((max_sum, tmp))

# 대각 1, 2
tmp1, tmp2 = 0, 0
for i in range(N):
    tmp1 += arr[i][i]
    tmp2 += arr[i][N - i - 1]
max_sum = max(max_sum, tmp1, tmp2)

print(max_sum)
