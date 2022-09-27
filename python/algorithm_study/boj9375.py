from collections import defaultdict

t = int(input())

for _ in range(t):
    maps = defaultdict(int)
    n = int(input())

    for _ in range(n):
        name, kind = input().split()
        maps[kind] += 1

    results = list(maps.values())

    tmp = 1
    for result in results:
        tmp *= (result + 1)

    print(tmp - 1)