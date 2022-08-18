n = int(input())
nums = sorted(list(map(int, input().split())))

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        print("D")
        break
else:
    print("U")