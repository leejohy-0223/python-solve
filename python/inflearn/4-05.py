from itertools import combinations

n, k = map(int, input().split())
nums = list(map(int, input().split()))

sums = set()
for results in combinations(nums, 3):  # 3중 for문으로도 가능
    sums.add(sum(results))

results = sorted(sums, reverse=True)
print(results[k - 1] if len(results) > k else -1)