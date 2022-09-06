def solution(id_list, report, k):
    answer = [0] * len(id_list)
    pick, picked = dict(), dict()
    for id in id_list:
        pick[id] = set()
        picked[id] = set()

    for rpt in report:
        p1, p2 = rpt.split(" ")
        # 신고 함
        pick[p1].add(p2)
        # 신고 당함
        picked[p2].add(p1)

    banUser = set()
    # picked에서 k보다 큰 key 출력
    for key in picked:
        if len(picked[key]) >= k:
            banUser.add(key)

    # pick에서 banUser를 가지고있는지 계산
    idx = 0
    for key, value in pick.items():
        answer[idx] = len(value & banUser)
        idx += 1
    id_list.index()

    return answer


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
