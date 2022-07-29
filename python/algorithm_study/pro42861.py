from collections import deque


def solution(n, costs):
    answer = 0
    costs = deque(sorted(costs, key=lambda x: x[2]))  # 비용기준으로 오름차순 정렬
    connect = {costs[0][0]}  # 첫 번째 커넥션을 집합에 넣기

    while len(connect) != n:
        cost = costs.popleft()
        if cost[0] in connect and cost[1] in connect:
            costs.append(cost)
            continue

        if cost[0] in connect or cost[1] in connect:
            connect.update([cost[0], cost[1]])
            answer += cost[2]
            continue

        costs.append(cost)

    return answer


if __name__ == '__main__':
    print(solution(7, [[0, 1, 29], [1, 2, 35], [2, 3, 7], [0, 4, 75], [4, 5, 53], [1, 5, 34], [5, 6, 25], [3, 6, 13],
                       [3, 5, 23]]))
    # print(solution(5, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [2, 3, 4], [3, 4, 7], [2, 4, 3]]))
    # print(solution(5, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [2, 3, 4], [3, 4, 7], [2, 4, 3]]))
