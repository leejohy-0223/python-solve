from bisect import bisect_left
from bisect import bisect_right

n, x = map(int, input().split())

sequence = list(map(int, input().split()))

left = bisect_left(sequence, x)
right = bisect_right(sequence, x)

print(left, right)
print(-1 if right == left else right - left)