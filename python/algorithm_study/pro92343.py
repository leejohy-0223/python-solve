lmap = []
allCount = 0
infos = []
chk = []
answer = 0


def dfs(wolfCount, sheepCount, possibleNode):
    global answer

    if wolfCount >= sheepCount:
        return

    answer = max(answer, sheepCount)

    # 로직 수행
    for node in possibleNode:
        if not chk[node]:
            chk[node] = True
            if infos[node] == 1:
                dfs(wolfCount + 1, sheepCount, possibleNode + lmap[node])
            else:
                dfs(wolfCount, sheepCount + 1, possibleNode + lmap[node])
            chk[node] = False


def solution(info, edges):
    global lmap, allCount, infos, chk
    infos = info
    allCount = len(info)
    chk = [False] * allCount
    lmap = [[] for _ in range(allCount)]

    for n1, n2 in edges:
        lmap[n1].append(n2)

    chk[0] = True
    dfs(0, 1, lmap[0].copy())
    return answer


if __name__ == '__main__':
    # print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    #                [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

    print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                   [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
