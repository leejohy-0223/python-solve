from collections import defaultdict


def solution(k, tangerine):
    values = defaultdict(int)
    for tg in tangerine:
        values[tg] += 1

    tmp = sorted(values.values(), reverse=True)
    answer, init = 0, 0
    for t in tmp:
        if init < k:
            init += t
            answer += 1
        else:
            return answer

    return answer

if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))