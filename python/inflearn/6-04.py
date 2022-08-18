from collections import deque

s, n = map(int, input().split())
works = list(map(int, input().split()))
cache = deque([0] * s)

for work in works:
    # 캐시에 없는 수라면
    if work not in cache:
        cache.appendleft(work)
        cache.pop()
    # 캐시에 있다면
    else:
        cache.remove(work)
        cache.appendleft(work)

print(" ".join(map(str, cache)))
