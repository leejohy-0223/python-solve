from sys import stdin
from itertools import combinations

def solution(n, k, strings):
    if k < 5:
        return 0
    k -= 5
    basicSet = {'a', 'c', 'i', 'n', 't'}
    allSet = set()
    for s in strings:
        allSet |= s

    diffSet = allSet - basicSet

    # 아예 조합을 만들 수 없는 경우는 전체 n 반환(모두 만들기 가능)
    if len(diffSet) <= k:
        return n

    answer = 0
    result = combinations(diffSet, k)

    for r in result:
        dictionary = basicSet | set(r)
        tmpAnswer = 0
        for s in strings:
            if s <= dictionary:
                tmpAnswer += 1
        answer = max(answer, tmpAnswer)
    return answer


if __name__ == '__main__':
    n1, k1 = map(int, stdin.readline().rstrip().split())
    values = []
    for _ in range(n1):
        values.append(set(stdin.readline().rstrip()))

    print(solution(n1, k1, values))