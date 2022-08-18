n, m = map(int, input().split())
songs = list(map(int, input().split()))

lo, hi = 0, 10001

while lo < hi:
    mid = (lo + hi) // 2

    # 담을 수 있는 앨범 계산
    count, tmpSum = 1, 0
    for song in songs:
        if tmpSum + song <= mid:
            tmpSum += song
        else:
            count += 1
            tmpSum = song

    if count <= m:
        hi = mid
    else:
        lo = mid + 1

print(lo)