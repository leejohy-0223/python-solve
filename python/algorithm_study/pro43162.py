chk = []
count = 0


def dfs(i, computers):
    for j in range(len(computers[i])):
        if computers[i][j] == 1 and not chk[j]:
            chk[j] = True
            dfs(j, computers)


def solution(n, computers):
    global chk, count
    chk = [False] * n

    for i in range(n):
        if not chk[i]:
            chk[i] = True
            count += 1
            dfs(i, computers)

    return count


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
