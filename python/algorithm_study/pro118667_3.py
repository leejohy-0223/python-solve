from collections import deque

halfSum = 0
sum1, sum2 = 0, 0
allLength = 0


def moveProperty(q1, q2, summation):
    dq1 = deque(q1)
    dq2 = deque(q2)
    cnt = 0
    while dq1 and dq2 and cnt <= allLength * 2:
        if summation == halfSum:
            return cnt
        elif summation < halfSum:
            value = dq2.popleft()
            dq1.append(value)
            summation += value
        else:
            value = dq1.popleft()
            dq2.append(value)
            summation -= value
        cnt += 1
    return -1


def solution(queue1, queue2):
    global halfSum, sum1, sum2, allLength
    sum1, sum2 = sum(queue1), sum(queue2)
    allSum = sum1 + sum2
    allLength = len(queue1) + len(queue2)

    if allSum % 2 != 0:
        return -1

    halfSum = allSum // 2
    return moveProperty(queue1, queue2, sum1)


if __name__ == '__main__':
    # print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    # print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
    # print(solution([2, 5, 2], [5]))
    # print(solution([5], [2, 5]))
    # print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1]))
    # print(solution([2], [2]))
    print(solution([1, 1, 1, 1, 1], [1, 1, 1, 9, 1]))
