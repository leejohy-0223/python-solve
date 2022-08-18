s, n = map(int, input().split())
works = list(map(int, input().split()))
cache = [0] * s

for work in works:
    if work not in cache:
        # 한 칸씩 모두 뒤로 밀기
        for i in range(s - 2, -1, -1):
             cache[i + 1] = cache[i]
    else:  # 캐시에 있다면
        idx = cache.index(work)
        # idx까지만 밀기
        for i in range(idx - 1, -1, -1):
            cache[i + 1] = cache[i]
    cache[0] = work


print(" ".join(map(str, cache)))
