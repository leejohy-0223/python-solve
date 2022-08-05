def solution(routes):
    sorted_routes = sorted(routes, key=lambda x: x[1])
    count = 1
    position = sorted_routes[0][1]

    for i in range(1, len(sorted_routes)):
        if sorted_routes[i][0] <= position <= sorted_routes[i][1]:
            continue
        else:
            count += 1
            position = sorted_routes[i][1]

    return count


if __name__ == '__main__':
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
