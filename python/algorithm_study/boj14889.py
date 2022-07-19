import sys
from itertools import combinations

n = int(input())

ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

people = [i for i in range(1, n + 1)]

result = 999999

chk_set = set()
for teamA in combinations(people, len(people) // 2):
    if teamA in chk_set:
        break

    teamB = list(set(people) - set(teamA))
    chk_set.update(teamA, teamB)

    sumA = 0
    sumB = 0

    for i in combinations(teamA, 2):
        sumA += (ability[i[0] - 1][i[1] - 1] + ability[i[1] - 1][i[0] - 1])

    for i in combinations(teamB, 2):
        sumB += (ability[i[0] - 1][i[1] - 1] + ability[i[1] - 1][i[0] - 1])

    result = min(result, abs(sumA - sumB))

print(result)
