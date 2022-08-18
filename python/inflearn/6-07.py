n = int(input())
position = []

for i in range(n):
    x, y = map(int, input().split())
    position.append((x, y))

position.sort(key=lambda tmp: (tmp[0], tmp[1]))

for x1, y1 in position:
    print(x1, y1, end="\n")
