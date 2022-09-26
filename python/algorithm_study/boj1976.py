unf = []


def find(v):
    if unf[v] == v:
        return v
    unf[v] = find(unf[v])
    return unf[v]


def union(i, j):
    x = find(i)
    y = find(j)
    if x != y:
        unf[x] = y


def solution(number, info, schedules):
    for i in range(number):
        for j in range(number):
            if info[i][j] == 1:
                union(i + 1, j + 1)

    length = len(schedules)
    for i in range(length - 1):
        if find(schedules[i]) != find(schedules[i + 1]):
            return "NO"

    return "YES"

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = []
    unf = [i for i in range(0, n + 1)]
    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))

    visit = list(map(int, input().split(" ")))
    print(solution(n, arr, visit))