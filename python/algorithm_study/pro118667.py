def solution(queue1, queue2):
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)

    if sumQ1 == sumQ2:
        return 0

    allSum = sumQ1 + sumQ2
    if allSum % 2 == 1:
        return -1

    halfSum = allSum // 2
    allArrays = queue1 + queue2
    lt, rt = 0, len(queue1) - 1
    result = sumQ1
    cnt = 0

    while result != halfSum:
        if lt == rt or rt == len(allArrays):
            return -1
        if result > halfSum:
            result -= allArrays[lt]
            lt += 1
        elif result < halfSum:
            rt += 1
            result += allArrays[rt] if rt < len(allArrays) else 0
        cnt += 1

    return cnt

if __name__ == '__main__':
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
    print(solution([1, 1], [1, 5]))
