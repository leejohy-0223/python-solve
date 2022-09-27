import heapq
import sys

n = int(input())

q = []
for _ in range(n):
    value = int(sys.stdin.readline())
    if value == 0:
        if not q:
            print("0")
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -value)
