import collections

answer = []
chk = False
graph = collections.defaultdict(list)
visited = collections.defaultdict(list)


def dfs(start, cnt, tmpList, length):
    global chk, answer
    if cnt == length:
        answer = tmpList
        chk = True
        return

    if chk:
        return

    for i in range(len(graph[start])):
        if not visited[start][i]:
            visited[start][i] = True
            dfs(graph[start][i], cnt + 1, tmpList + [graph[start][i]], length)
            visited[start][i] = False


def solution(tickets):
    for depart, arrival in tickets:
        graph[depart].append(arrival)
        visited[depart].append(False)
    for depart, arrival in graph.items():
        graph[depart].sort()

    dfs("ICN", 0, ["ICN"], len(tickets))

    return answer


if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
    # print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))
