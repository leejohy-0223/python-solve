import sys

input = sys.stdin.readline
n, c = map(int, input().split())

house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

left, right = house[1] - house[0], house[-1] - house[0]
result = 0

while left <= right:
    mid = (left + right) // 2

    min_pos = house[0]
    count = 1
    for i in range(1, n):
        if house[i] >= min_pos + mid:
            min_pos = house[i]
            count += 1

    if count >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)
