N = int(input())
nums = list(map(int, input().split()))

result = str(nums[0]) + " "
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        result += str(nums[i]) + " "

print(result)