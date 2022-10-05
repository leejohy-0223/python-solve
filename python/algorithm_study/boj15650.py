from itertools import combinations

n, m = map(int, input().split())
arr = list(range(1, n + 1))
results = combinations(arr, m)

for result in results:
    print(' '.join(map(str, result)))
