N = int(input())
nums = list(map(int, input().split()))

result, accumulate = nums[0], nums[0]
for i in range(1, N):
    if nums[i] == 0:
        accumulate = 0
    else:
        accumulate += 1
        result += accumulate

print(result)
