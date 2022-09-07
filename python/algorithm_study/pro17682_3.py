def solution(dartResult):
    dart = {'S': 1, 'D': 2, 'T': 3}
    scores = []
    numStart = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[numStart:i]) ** dart[d])
        if d == "*":
            scores[-2:] = [x * 2 for x in scores[-2:]]  # 맨 끝 숫자 2개만 2배해서 갱신
        if d == "#":
            scores[-1] = (-1) * scores[-1]
        if not d.isnumeric():  # 숫자가 아니라면 n에 i + 1을 할당
            numStart = i + 1

    return sum(scores)


if __name__ == '__main__':
    # print(solution("1S2D*3T"))
    print(solution("1D2S#10S"))
    # print(solution("1S*2T*3S"))
