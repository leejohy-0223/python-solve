from collections import deque


def bfs():
    s, e = map(int, input().split())
    go = [1, -1, 5]
    q = deque([s])
    chk = [False] * 10001
    chk[s] = True
    depth = 0
    while q:
        size = len(q)
        for i in range(size):
            now = q.popleft()
            if now == e:
                return depth
            for g in go:
                nxt = now + g
                if 1 <= nxt <= 10000 and not chk[nxt]:
                    chk[nxt] = True
                    q.append(nxt)
        depth += 1


print(bfs())
