from collections import defaultdict

accumulate = defaultdict(int)


def pick(first, second):
    if accumulate[first] == accumulate[second]:
        return first
    return first if accumulate[first] > accumulate[second] else second


def solution(survey, choices):
    answer = ''
    for idx, sur in enumerate(survey):
        first, second = sur
        if choices[idx] < 4:
            accumulate[first] += 4 - choices[idx]
        elif choices[idx] > 4:
            accumulate[second] += choices[idx] - 4

    answer += pick('R', 'T')
    answer += pick('C', 'F')
    answer += pick('J', 'M')
    answer += pick('A', 'N')

    return answer


if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
