def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = ['S', 'D', 'T']
    for p in point:
        if p in sdt:
            answer[i] = answer[i] ** (sdt.index(p) + 1)
        elif p == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif p == '#':
            answer[i] = answer[i] * -1
        else:
            answer.append(int(p))
            i += 1
    return sum(answer)

if __name__ == '__main__':
    # print(solution("1S2D*3T"))
    print(solution("1D2S#10S"))
    # print(solution("1S*2T*3S"))