def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        curArray = triangle[i]
        for j in range(len(curArray)):
            if j == 0:
                dp[i].append(dp[i - 1][0] + curArray[j])
            elif j == len(curArray) - 1:
                dp[i].append(dp[i - 1][-1] + curArray[j])
            else:
                dp[i].append(max(dp[i - 1][j - 1], dp[i - 1][j]) + curArray[j])

    return max(dp[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
