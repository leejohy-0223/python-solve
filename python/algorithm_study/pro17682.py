# now에 현재 범위를 담고,

def solution(dartResult):
    answer = 0
    idx, start, length = 1, 0, len(dartResult)
    before = 0
    while idx < length:
        while idx < length and dartResult[idx].isdigit():
            idx += 1
        while idx < length and not dartResult[idx].isdigit():
            idx += 1
        now = dartResult[start:idx]
        tmpnums = int(now[0]) if not now[1].isdigit() else int(now[0:2])

        tmpResult = 0
        if 'S' in now:
            tmpResult += tmpnums
        elif 'D' in now:
            tmpResult += pow(tmpnums, 2)
        else:
            tmpResult += pow(tmpnums, 3)

        if '*' in now:
            answer -= before
            answer += before * 2
            tmpResult *= 2
        elif '#' in now:
            tmpResult *= -1
        answer += tmpResult
        before = tmpResult
        start = idx
        idx += 1

    return answer

if __name__ == '__main__':
    # print(solution("1S2D*3T"))
    # print(solution("1D2S#10S"))
    print(solution("1S*2T*3S"))