n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
result = 0
summation = nums[0]

while right < n:
    if summation < m:
        right += 1
        if right < n:
            summation += nums[right]
    elif summation == m:
        result += 1
        right += 1
        if right < n:
            summation += nums[right]
    else:
        summation -= nums[left]
        left += 1

print(result)