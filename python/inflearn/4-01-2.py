from collections import defaultdict

n = int(input())
strings = input()
maps = defaultdict(int)
for i in strings:
    maps[i] += 1

mx, result = 0, 0
for k, v in maps.items():
    if v > mx:
        mx = v
        result = k

print(result)
