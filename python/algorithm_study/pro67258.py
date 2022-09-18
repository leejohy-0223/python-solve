from collections import defaultdict

def solution(gems):
    gems_pos = defaultdict(int)
    all_size = len(set(gems))
    left = right = 0
    results = []

    while right < len(gems):
        # right에 있는 값을 dict에 넣기
        gems_pos[gems[right]] += 1

        # 현재 범위(left ~ right)에 모든 보석이 있다면, left를 올리기
        while len(gems_pos) == all_size:
            gems_pos[gems[left]] -= 1
            if not gems_pos[gems[left]]:
                del gems_pos[gems[left]]
            results.append((left, right))
            left += 1
        right += 1

    results.sort(key=lambda result: (result[1] - result[0], result[0]))
    return [results[0][0] + 1] + [results[0][1] + 1]

if __name__ == '__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
    # print(solution(["AA", "AB", "AA", "AC", "AA", "AD", "AC", "AA", "AB", "AC", "AD", "AB", "AD", "AA", "AA", "AC", "AC", "AD", "AA"]))
    # print(solution(["AA", "AB", "AC", "AA", "AC"]))
    # print(solution(["XYZ", "XYZ", "XYZ"]))
