n = int(input())
nArray = list(map(int, input().split()))

m = int(input())
mArray = list(map(int, input().split()))

result = []
i, j = 0, 0
while i < n and j < m:
    if nArray[i] >= mArray[j]:
        result.append(mArray[j])
        j += 1
    else:
        result.append(nArray[i])
        i += 1

if i != n:
    result += nArray[i:]
elif j != m:
    result += mArray[j:]

print(" ".join(map(str, result)))