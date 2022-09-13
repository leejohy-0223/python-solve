answer = 0
visited = []


def dfs(k, dungeons, depth):
    global answer
    global visited
    answer = max(depth, answer)
    for i, dungeon in enumerate(dungeons):
        if not visited[i] and k >= dungeon[0]:
            visited[i] = True
            dfs(k - dungeon[1], dungeons, depth + 1)
            visited[i] = False


def solution(k, dungeons):
    global visited
    visited = [False] * len(dungeons)
    dfs(k, dungeons, 0)
    return answer

if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
