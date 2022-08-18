answer = []


def DFS(start, countryArray, count, allCount, used, tickets):
    global answer
    if count == allCount:
        if not answer:
            answer = countryArray.copy()
        else:
            answer = countryArray.copy() if "".join(answer) > "".join(countryArray) else answer
        return

    for i in range(len(tickets)):
        if tickets[i][0] == start and not used[i]:
            used[i] = True
            countryArray.append(tickets[i][1])

            DFS(tickets[i][1], countryArray, count + 1, allCount, used, tickets)

            used[i] = False
            countryArray.pop()


def solution(tickets):

    start = "ICN"
    used = [False] * len(tickets)
    DFS(start, ["ICN"], 0, len(tickets), used, tickets)

    return answer

if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))