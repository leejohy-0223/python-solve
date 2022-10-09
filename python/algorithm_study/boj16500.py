S = input()
length = len(S)
dp = [0] * (length + 1)
dp[length] = 1
n = int(input())
strings = [input() for _ in range(n)]

for i in range(length, -1, -1):
    for string in strings:
        if S.find(string, i) == i and dp[i + len(string)] == 1:
            dp[i] = 1
            break

print(dp[0])


