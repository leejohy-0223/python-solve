N = int(input())
arr = []
chk = [[False] * N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if not chk[i][j]:
            chk[i][j] = True
            now, tmpChk = arr[i][j], True
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if now > arr[nx][ny]:
                    chk[nx][ny] = True
                else:
                    tmpChk = False

            if tmpChk:
                cnt += 1

print(cnt)



