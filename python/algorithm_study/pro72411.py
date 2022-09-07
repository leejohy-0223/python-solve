# course 배열의 수만큼의 조합을 만들고,
# 모든 조합에 대해 모든 order를 비교한다.
# set으로 변환해서 포함되는 수를 count하고, maxCount를 갱신하거나 같을 경우에만 tmpAnswer에 넣는다.
# 해당 course에서 가장 많은 선택을 받은 결과를 string으로 반환해서 answer에 넣는다.

from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        # c개 조합을 만들기
        mxCount = 0
        tmpAnswers = set()
        for order in orders:
            for com in list(combinations(order, c)):
                com = tuple(sorted(com))
                if com in tmpAnswers:
                    continue
                # 조합을 대상으로 다른 order에 포함되는 횟수 구하기
                target = set(com)
                count = 0
                for odr in orders:
                    if not target.difference(odr):
                        count += 1

                # 2개 이상일 경우 후보에 넣기
                if count >= 2 and mxCount <= count:
                    if mxCount < count:
                        tmpAnswers = {com}
                        mxCount = count
                    else:
                        tmpAnswers.add(com)

        for tmp in tmpAnswers:
            answer.append(''.join(tmp))

    return sorted(answer)


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    # print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
    # tmpSet = {(1, 2)}
    # tmpSet.add((2, 3))
    # print(tmpSet)

