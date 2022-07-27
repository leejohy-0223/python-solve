import copy
from collections import deque


def solution(name):
    moves = [-1, 1]
    nameList = list(name)

    # start = (nameList, index, count)
    dq = deque([(nameList, 0, 0)])
    while dq:
        arr, idx, count = dq.pop()
        # 현 위치의 내용을 A로 변경한다.
        count += min(ord(arr[idx]) - 65, 91 - ord(arr[idx]))
        arr[idx] = 'A'

        if arr.count('A') == len(name):
            return count

        for move in moves:
            dq.appendleft((copy.deepcopy(arr), idx + move, count + 1))

if __name__ == '__main__':
    # print(solution("AAABBBABA"))

    dq2 = deque([[3, 2]])
    dq2.append([2])

    print(dq2)
