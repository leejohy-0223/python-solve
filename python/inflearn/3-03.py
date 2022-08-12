n, k = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, k - 1
mSum = sum(nums[left: right + 1])
tmpSum = mSum
while right < n - 1:
    #  left 빼고 올리기
    tmpSum -= nums[left]
    left += 1
    right += 1
    tmpSum += nums[right]
    mSum = max(mSum, tmpSum)

print(mSum)
