from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    count, i = 0, 0

    while people:
        now = people.popleft()
        count += 1
        while people and (people[-1] + now) > limit:
            people.pop()
            count += 1
        if people:
            people.pop()

    return count


if __name__ == '__main__':
    print(solution([70, 80, 50], 100))
    # print(solution([20, 30, 20, 50, 70, 80], 70))
