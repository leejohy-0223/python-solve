arrowCount, appeach = 0, []
result = []
mx_diff = 0


def permu(template):
    global mx_diff
    if len(template) == 10:
        tmpArrowCount = arrowCount
        tmpResult = [0] * 11
        ap_score, rian_score = 0, 0
        for idx, t in enumerate(template):
            # 승리할 수 없는 경우는 화살 아끼기
            if t == 0:
                if appeach[idx]:
                    ap_score += (10 - idx)
                continue

            # 승리해야하는 경우는 화살 사용 (어피치보다 하나 더 쓰기)
            usedArrow = appeach[idx] + 1
            tmpArrowCount -= usedArrow

            # 화살 안남았으면 return
            if tmpArrowCount < 0:
                return

            rian_score += (10 - idx)
            tmpResult[idx] = usedArrow

        if tmpArrowCount > 0:
            tmpResult[-1] = tmpArrowCount

        if mx_diff <= rian_score - ap_score != 0:
            if mx_diff < rian_score - ap_score:
                mx_diff = rian_score - ap_score
                result.clear()
            result.append(tmpResult)
        return

    for i in range(0, 2):
        permu(template + [i])


def string_convert(r):
    s = list(map(str, r[::-1]))
    return ''.join(s)


def solution(n, info):
    global arrowCount, appeach
    arrowCount = n
    appeach = info
    permu([])
    results = sorted(result, key=lambda r: string_convert(r))[-1] if len(result) != 0 else [-1]

    return results


if __name__ == '__main__':
    # print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
    print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
    # print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # tmp = []
    # tmp.append([1, 2, 3])
    # tmp.append([1, 3, 4])
    # print(tmp)
