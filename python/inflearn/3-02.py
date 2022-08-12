n = int(input())
nArray = sorted(list(map(int, input().split())))

m = int(input())
mArray = sorted(list(map(int, input().split())))

i, j = 0, 0
result = []
while i < n and j < m:
    if nArray[i] > mArray[j]:
        j += 1
    elif nArray[i] < mArray[j]:
        i += 1
    else:
        result.append(nArray[i])
        i += 1
        j += 1

print(" ".join(map(str, result)))