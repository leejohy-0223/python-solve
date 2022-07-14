n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(min(list(map(int, input().split()))))

print(max(arr))
