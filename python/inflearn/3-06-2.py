n, k = map(int, input().split())
nums = list(map(int, input().split()))

lt = 0
cnt, result = 0, 0
for rt in range(n):
    # rt의 위치가 0이면 1로 변경
    if nums[rt] == 0:
        cnt += 1

    # 변경이 불가능하다면 1로 바뀌었다고 가정된 부분을 다시 0으로 변경
    while cnt > k:
        if nums[lt] == 0:
            cnt -= 1
        lt += 1

    # 변경 후 결과 갱신
    result = max(result, rt - lt + 1)

print(result)