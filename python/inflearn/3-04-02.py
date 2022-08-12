n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
result = 0
summation = nums[0]

#  같거나 크면 lt위치 빼고 lt += 1
#  작으면 rt위치 올리고 더하기
while right < n:
    if summation >= m:
        result += 1 if summation == m else 0
        summation -= nums[left]
        left += 1
    else:
        right += 1
        summation += nums[right] if right < n else 0

print(result)