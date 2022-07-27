def solution(n, lost, reserve):
    #  우선 자신의 도난당했을 경우를 대비해서 한 번 체크
    n_reserve = [r for r in reserve if r not in lost]
    n_lost = [l for l in lost if l not in reserve]

    resolve_count = 0
    for i in n_lost:
        if i - 1 in n_reserve:
            n_reserve.remove(i - 1)
            resolve_count += 1
        elif i + 1 in n_reserve:
            n_reserve.remove(i + 1)
            resolve_count += 1

    return n - (len(n_lost) - resolve_count)

if __name__ == '__main__':
    # print(solution(3, [1, 2], [2, 3]))

    arr = [1, 2, 3]
    print(arr[-3])
