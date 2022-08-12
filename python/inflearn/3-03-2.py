#  left, right 두지 말고 right 기준으로 왼쪽으로 right - k에 있는 녀석을 빼도 좋다.

n, k = map(int, input().split())
nums = list(map(int, input().split()))

right = k - 1
mSum = sum(nums[0: right + 1])
tmpSum = mSum

for i in range(right + 1, n):
    tmpSum += (nums[i] - nums[i - k])
    mSum = max(mSum, tmpSum)

print(mSum)
