import decimal


class Time:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime


def solution(lines):
    answer = 0
    timeInfos = []
    for line in lines:
        y, hms, duration = line.split(" ")
        h, m, s = hms.split(":")
        endTime = float(h) * 3600 + float(m) * 60 + float(s)
        startTime = float(endTime - float(duration[:-1])) + 0.001
        startTime = float('{:.3f}'.format(decimal.Decimal(str(startTime))))
        timeInfos.append(Time(startTime, endTime))

    Length = len(timeInfos)
    for start in range(Length):
        endSecond = timeInfos[start].endTime + 1
        tmpCount = 1
        for now in range(start + 1, Length):
            if endSecond > timeInfos[now].startTime:
                tmpCount += 1
        answer = max(answer, tmpCount)

    return answer


if __name__ == '__main__':
    print(solution([
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]))
    # print(solution([
    #     "2016-09-15 01:00:04.002 2.0s",
    #     "2016-09-15 01:00:07.000 2s"
    # ]))

    # print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
    # print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    # print(1.001 < 1.003)