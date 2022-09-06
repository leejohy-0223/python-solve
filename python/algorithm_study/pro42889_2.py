from collections import defaultdict


def solution(N, stages):
    numberCount = defaultdict(int)
    # dict를 다음처럼 초기화하면, return에서 초기화해줄 필요 없다.
    failScore = {i: 0 for i in range(1, N + 1)}

    for stage in stages:
        numberCount[stage] += 1

    curNumber, curLength = 1, len(stages)
    while curNumber <= N and curLength != 0:
        failScore[curNumber] = numberCount[curNumber] / curLength
        curLength -= numberCount[curNumber]
        curNumber += 1

    sorted_score = sorted(failScore.items(), key=lambda score: (-score[1], score[0]))
    return [i[0] for i in sorted_score]


if __name__ == '__main__':
    # print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # print(solution(5, [1, 2, 3, 4]))
    # print(solution(1, [2]))
    print(solution(6, [4, 4, 4, 4, 4, 5, 5, 5]))
    # print(solution(4, [4, 4, 4, 4, 4]))
