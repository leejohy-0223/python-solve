from bisect import bisect

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

print(bisect(nums, m))
