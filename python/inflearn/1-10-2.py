st, target = input().split()

dist = [0] * len(st)
value = 111

for i in range(len(st)):
    if st[i] == target:
        value = 0
    dist[i] = value
    value += 1

value = 111
for i in range(len(st) - 1, -1, -1):
    if st[i] == target:
        value = 0
    dist[i] = min(dist[i], value)
    value += 1

print(" ".join(map(str, dist)))
