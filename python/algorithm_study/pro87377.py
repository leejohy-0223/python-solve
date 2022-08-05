def solution(line):
    result = []
    for i in range(0, len(line) - 1):
        A, B, E = line[i]
        for j in range(i + 1, len(line)):
            C, D, F = line[j]
            denominator = (A * D) - (B * C)
            if denominator == 0:
                continue

            x = ((B * F) - (E * D)) // denominator
            y = ((E * C) - (A * F)) // denominator

            if ((B * F) - (E * D)) % denominator == 0 and ((E * C) - (A * F)) % denominator == 0:
                result.append([x, y])

    xs = [r[0] for r in result]
    x_min = min(xs)
    x_max = max(xs)

    ys = [r[1] for r in result]
    y_min = min(ys)
    y_max = max(ys)

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for r in result:
        x, y = r
        answer[y - y_min][x - x_min] = "*"

    return [''.join(ans) for ans in answer][::-1]

if __name__ == '__main__':
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    # print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    # print(solution([[1, -1, 0], [2, -1, 0]]))
    # print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
    # print(solution([]))
