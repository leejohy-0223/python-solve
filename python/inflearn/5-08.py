from collections import deque


def solution():
    N, M = map(int, input().split())
    patients = list(map(int, input().split()))
    q = deque([Person(num, p) for num, p in enumerate(patients)])

    cnt = 1
    while q:
        now = q.popleft()
        for i in q:
            if i.priority > now.priority:
                q.append(now)
                break
        else:
            if now.nums == M:
                return cnt
            cnt += 1


class Person:
    def __init__(self, nums, priority):
        self.nums = nums
        self.priority = priority

if __name__ == '__main__':
    print(solution())