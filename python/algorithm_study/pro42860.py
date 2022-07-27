def solution(name):

    # 길이만큼 초기화
    length = len(name)

    # 고쳐야 할 곳의 index를 list에 담기
    fix_need = []
    for i, value in enumerate(name):
        if value != 'A':
            fix_need.append(i)

    # 최초 인덱스
    idx = 0
    count = 0
    # 가야할 곳 정하기
    while len(fix_need) != 0:
        min_dist = 30
        next_idx = 0
        for target in fix_need:
            # 정방향
            forward_dist = abs(target - idx)

            # 역방향
            backward_dist = abs(idx + (length - target))

            # 둘 중 최소
            dist = min(forward_dist, backward_dist)

            if min_dist > dist:
                min_dist = dist
                next_idx = target

        # 다음 인덱스를 list에서 제거
        fix_need.remove(next_idx)

        # 현재 인덱스 갱신
        idx = next_idx
        count += min_dist

        print("cur idx : ", idx, "summation : ", min_dist)

        # 이동
        # print(ord('J') - ord('B'))  # 정방향
        # print(ord('B') - ord('A') + (ord('Z') - ord('J')) + 1)  # 역방향

        # 정방향 길이
        forward_len = ord(name[idx]) - ord('A')

        # 역방향 길이
        backward_len = ord('Z') - ord(name[idx]) + 1 if name[idx] != 'Z' else 0

        # 계산
        print(forward_len, backward_len)
        print(" === ")
        count += min(forward_len, backward_len)

    return count

if __name__ == '__main__':
    # print(solution("JAN"))
    # print(solution("JEROEN"))
    print(solution("AAABBBABA"))
