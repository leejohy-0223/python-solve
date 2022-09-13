def solution(levels):
    if len(levels) < 4:
        return -1

    results = sorted(levels, reverse=True)
    idx = len(levels) // 4
    return results[idx - 1]


if __name__ == '__main__':
    # print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution([1, 2]))