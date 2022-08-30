from collections import deque


def solution(queue1, queue2):
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)

    if sumQ1 == sumQ2:
        return 0

    allSum = sumQ1 + sumQ2
    if allSum % 2 == 1:
        return -1

    halfSum = allSum // 2

    r1 = calculate(queue1, queue2, sumQ1, halfSum)
    r2 = calculate(queue2, queue1, sumQ2, halfSum)

    if r1 == -1:
        return r2
    elif r2 == -1:
        return r1
    else:
        return min(r1, r2)


def calculate(arr1, arr2, result, halfSum):
    q1 = deque(arr1)
    q2 = deque(arr2)
    cnt = 0
    while q1 and q2:
        if result < halfSum:
            tmp = q2.popleft()
            result += tmp
            q1.append(tmp)
        elif result > halfSum:
            result -= q1.popleft()
        else:
            return cnt
        cnt += 1

    return -1

if __name__ == '__main__':
    print(solution([4, 6, 5, 1], [3, 2, 7, 2]))
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
    print(solution([1, 1], [1, 5]))
