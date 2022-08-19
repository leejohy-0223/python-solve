result = "NO"


def DFS(chk, nums, L):
    global result
    if L == len(nums):
        sum1 = sum2 = 0
        for idx, c in enumerate(chk):
            if c:
                sum1 += nums[idx]
            else:
                sum2 += nums[idx]
        if sum1 == sum2:
            result = "YES"
        return
    else:
        chk[L] = True
        DFS(chk, nums, L + 1)

        chk[L] = False
        DFS(chk, nums, L + 1)


def solution():
    n = int(input())
    nums = list(map(int, input().split()))

    chk = [False] * n
    DFS(chk, nums, 0)

    return result


print(solution())
