def solution(N, stages):
    fail_score = dict()

    cur_stage = 1
    count, cur_length, length = 0, len(stages), len(stages)
    stages.sort()

    pos = 0
    while pos < length:
        while pos < length and stages[pos] == cur_stage:
            count += 1
            pos += 1
        fail_score[cur_stage] = count / cur_length
        cur_length -= count
        count = 0
        cur_stage += 1

    sorted_score = sorted(fail_score.items(), key=lambda score: (-score[1], score[0]))
    answer = [i[0] for i in sorted_score if i[0] <= N]

    # 검사가 되지 않은 stage 추가 (예를 들어 6단계까지 있는데 4까지만 탐색되었다면 5, 6을 추가해줘야 한다.)
    added = len(answer) + 1
    while len(answer) < N:
        answer.append(added)
        added += 1

    return answer


if __name__ == '__main__':
    # print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # print(solution(5, [1, 2, 3, 4]))
    # print(solution(1, [2]))
    print(solution(4, [4, 4, 4, 4, 4, 5, 5, 5]))
