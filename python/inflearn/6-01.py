n = int(input())
nums = list(map(int, input().split()))

for i in range(n - 1):
    idx = i
    minNum = nums[i]
    for j in range(i, n):
        if minNum > nums[j]:
            idx = j
            minNum = nums[j]
    nums[i], nums[idx] = nums[idx], nums[i]

print(" ".join(map(str, nums)))
