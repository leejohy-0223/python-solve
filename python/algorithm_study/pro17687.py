def convert(n, base):
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    longStrings, start = '', 0
    idx = p
    while len(answer) != t:
        longStrings += convert(start, n)

        # answer 갱신
        while idx <= len(longStrings) and len(answer) != t:
            answer += longStrings[idx - 1]
            idx += m
        start += 1

    return answer


if __name__ == '__main__':
    # print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))