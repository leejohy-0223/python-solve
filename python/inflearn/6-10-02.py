n, count = map(int, input().split())
stall = sorted(list(map(int, input().split())))

lt = stall[0]
rt = stall[-1]
answer = 0
while lt <= rt:
    mid = (lt + rt) // 2

    hCount, pos = 1, stall[0] + mid
    for i in range(1, len(stall)):
        if stall[i] >= pos:
            pos = (stall[i] + mid)
            hCount += 1

    if hCount >= count:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)