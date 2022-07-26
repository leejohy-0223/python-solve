def solution(sizes):
    res_max, res_min = 0, 0
    for size in sizes:
        res_max = max(res_max, max(size))
        res_min = max(res_min, min(size))

    return res_max * res_min



if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))