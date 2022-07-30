n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = []
i, j = 0, 0

while i < n or j < m:
    # a 쪽이 작다면 a를 result에 넣기
    if j >= m or (i < n and a[i] < b[j]):
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

print(result)