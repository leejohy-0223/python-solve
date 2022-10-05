n, m = map(int, input().split())


def nCr(n, r):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, i + 1):
            if j - 1 < 0:
                dp[i][j] = dp[i - 1][0]
            elif j >= i:
                dp[i][j] = dp[i - 1][i - 1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][r]

print(nCr(n, m))