from itertools import combinations


def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(1, len(nums) // 2 + 1):
        result = combinations(nums, i)
        for r in result:
            tmpList = list(r)
            remainderList = list(set(nums) - set(tmpList))
            if sum(tmpList) == sum(remainderList):
                return "YES"
    return "NO"


print(solution())
