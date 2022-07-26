n = int(input())

nums = list(map(int, input().split()))

start = 0
end = n - 1

result = -1

while start <= end:
    mid = (start + end) // 2
    if mid == nums[mid]:
        result = mid
        break
    elif mid < nums[mid]:
        end = mid - 1
    else:
        start = mid + 1

print(result)



