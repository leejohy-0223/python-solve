dp = [0] * 101
dp[0], dp[1], dp[2], dp[3], dp[4] = 0, 1, 1, 1, 2

lft = 0
for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[lft]
    lft += 1

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])