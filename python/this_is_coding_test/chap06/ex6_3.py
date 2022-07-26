n, k = map(int, input().split())

arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if arrA[i] < arrB[i]:
        arrA[i] = arrB[i]
    else:
        break

print(sum(arrA))
