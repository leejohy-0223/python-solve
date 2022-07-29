def solution(n, costs):
    answer = 0
    sorted_cost = sorted(costs, key=lambda x: x[2])
    connect = {costs[0][0]}

    while len(connect) != n:
        for cost in sorted_cost:
            if cost[0] in connect and cost[1] in connect:
                sorted_cost.remove(cost)
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                sorted_cost.remove(cost)
                break

    return answer


if __name__ == '__main__':
    print(solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53],
                       [0, 4, 75]]))
