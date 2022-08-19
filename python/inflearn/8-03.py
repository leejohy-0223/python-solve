def dfs(scores, sumTime, L, aScore):
    global maxScore
    if sumTime > m or allScore - aScore + scores < maxScore:
        return
    if L == n:
        maxScore = max(maxScore, scores)
    else:
        dfs(scores + quiz[L][0], sumTime + quiz[L][1], L + 1, aScore + quiz[L][0])
        dfs(scores, sumTime, L + 1, aScore + quiz[L][0])

allScore = 0
maxScore = 0
n, m = map(int, input().split())
quiz = []

for _ in range(n):
    score, time = map(int, input().split())
    quiz.append([score, time])
    allScore += score

dfs(0, 0, 0, 0)
print(maxScore)