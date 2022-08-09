from collections import deque

st, target = input().split()

dist = [-1] * len(st)
chk = [False] * len(st)
chklist = deque()
for idx, char in enumerate(st):
    if char == target:
        dist[idx] = 0
        chk[idx] = True
        chklist.append(idx)

while chklist:
    now = chklist.popleft()
    # 왼쪽
    if now - 1 >= 0 and not chk[now - 1]:
        chk[now - 1] = True
        dist[now - 1] = dist[now] + 1
        chklist.append(now - 1)

    # 오른쪽
    if now + 1 < len(st) and not chk[now + 1]:
        chk[now + 1] = True
        dist[now + 1] = dist[now] + 1
        chklist.append(now + 1)

print(" ".join(map(str, dist)))
