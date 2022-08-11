N = int(input())
chk = [False] * (N + 1)

cnt = 0
for i in range(2, N + 1):
    if not chk[i]:
        chk[i] = True
        cnt += 1
        for j in range(i, N + 1, i):
            chk[j] = True

print(cnt)
