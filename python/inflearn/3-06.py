n, k = map(int, input().split())
nums = list(map(int, input().split()))

#  lt : 1을 0으로 바꾼다고만 가정
#  rt : 0을 1로 바꾼다고만 가정

lt = 0
result = -1
cnt = 0
for rt in range(n):
    #  0이라면 일단 rt위치에 있는 cnt를 올려준다.
    if nums[rt] == 0:
        cnt += 1

    #  cnt가 유효한지 검증한다.
    while cnt > k:
        # lt위치 값이 0이라면 cnt를 내린다.
        if nums[lt] == 0: # 실제로 변경한게 아니기 때문에 0인 부분(rt가 1로 변경했다고 가정한)을 체크한다.
            cnt -= 1
        # 값이 1이라면 0 만날때까지 lt를 올린다.
        lt += 1

    result = max(result, rt - lt + 1)

print(result)


