def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]  # 스택의 최상단 탐험
        if top not in routes or len(routes[top]) == 0:  # 스택의 맨 위에 있는 값이 routes에 없거나, routes[top]에 아무것도 연결 안됐다면?
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])  # 값이 있다면 top에 연결된 가장 빠른 이름을 가진 공항 넣기
            routes[top] = routes[top][:-1]  # 맨 뒤에꺼 제거하고 리스트 갱신
    return path[::-1]  # 역순으로 출력

if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
    print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))