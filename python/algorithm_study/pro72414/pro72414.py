# 누적합 핵심 -> 모든 내용을 누적한 후 계산해준다.

def str_to_int(str_time):
    h, m, s = str_time.split(":")
    return 3600 * int(h) + 60 * int(m) + int(s)


def resolveToStr(num_time):
    h = num_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    num_time = num_time % 3600
    m = num_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    num_time = num_time % 60
    s = '0' + str(num_time) if num_time < 10 else str(num_time)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    # 시간을 누적할 보드
    time_board = [0 for _ in range(play_time + 1)]

    # 시작, 끝 시간을 마킹
    for log in logs:
        start, end = log.split("-")
        start = str_to_int(start)
        end = str_to_int(end)
        time_board[start] += 1
        time_board[end] -= 1

    # 마킹된 수를 기반으로 초마다 시청자수 기록
    for i in range(1, len(time_board)):
        time_board[i] += time_board[i - 1]

    # 한번 더 수행해서 누적합 기록
    for i in range(1, len(time_board)):
        time_board[i] += time_board[i - 1]

    # 결과적으로, time_board[x] = 시각 0부터 x까지 x + 1 초 간의 구간을 포함하는 누적 재생 시간

    # 최대 긴 구간을 구하고 시작시간 체크하기
    most_view = 0
    max_time = 0

    for i in range(adv_time - 1, len(time_board)):
        if i >= adv_time:
            if time_board[i] - time_board[i - adv_time] > most_view:
                most_view = time_board[i] - time_board[i - adv_time]
                # 광고 러닝타임이 3(adv_time), 현재 갱신된 범위가 3 ~ 5(i) 라고 가정하자.
                # 우리는 여기에서 광고 시작시간인 3을 구해야 하므로, 5(i) - 3 + 1 = 3으로 간단히 구한다.
                max_time = i - adv_time + 1
        else:
            if time_board[i] > most_view:
                most_view = time_board[i]
                max_time = i - adv_time + 1

    return resolveToStr(max_time)


if __name__ == '__main__':
    # print(solution("02:03:55", "00:14:15",
    #                ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
    #                 "01:37:44-02:02:30"]))

    print(solution("99:59:59",
                   "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))