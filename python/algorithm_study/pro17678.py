def timeToMin(timetable):
    results = []
    for time in timetable:
        h, m = map(int, time.split(":"))
        results.append(h * 60 + m)
    return results


def resolveToTime(minute):
    h, m = str(minute // 60), str(minute % 60)
    h = h if len(h) == 2 else '0' + h
    m = m if len(m) == 2 else '0' + m
    return "{}:{}".format(h, m)


def solution(n, t, m, timetable):
    minute_time_table = sorted(timeToMin(timetable))

    curBusTime = 540
    lastBusTime = curBusTime + (n - 1) * t
    idx, count = 0, 0

    while True:
        # 현재 탈 사람이 lastBus보다 늦게 오는 사람이라면 어차피 못타므로 반환하기
        if minute_time_table[idx] > lastBusTime:
            return resolveToTime(lastBusTime)

        # 끝 버스에 왔으면 탈 수 있는지 체크
        if curBusTime == lastBusTime:
            # 남은 사람 다 탈 수 있다면 가능
            if len(minute_time_table) - idx < m:
                return resolveToTime(lastBusTime)
            # 못타는 경우 새치기
            else:
                lastIdx = len(minute_time_table) - 1
                while lastIdx - idx + 1 != m:
                    lastIdx -= 1

                return resolveToTime(minute_time_table[lastIdx] - 1)

        # 사람 태우기
        if minute_time_table[idx] <= curBusTime and count < m:
            idx += 1
            count += 1

        # 인원 다 채워지거나, 현재 idx가 curBusTime보다 늦다면 curBusTime 올리기
        if count == m or minute_time_table[idx] > curBusTime:
            count = 0
            curBusTime += t


if __name__ == '__main__':
    # print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    # print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(1, 1, 1, ["23:59"]))
