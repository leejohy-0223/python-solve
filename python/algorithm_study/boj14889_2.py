# https://www.acmicpc.net/source/38805493

import sys
from itertools import combinations

n = int(input())

# 0 1 2 3
# 4 0 5 6 ...

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
team_stat = [sum(x) + sum(y) for x, y in zip(arr, zip(*arr))]
all_team_stat = sum(team_stat) // 2

answer = 40001
for n in combinations(team_stat, n//2):
    answer = min(answer, abs(all_team_stat - sum(n)))

