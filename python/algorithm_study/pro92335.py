import math


def primenumber(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def convert(n, base):
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, k):
    answer = 0
    results = [result for result in convert(n, k).split("0") if result != ""]

    for r in results:
        if primenumber(int(r)):
            answer += 1

    return answer


if __name__ == '__main__':
    # print(solution(437674, 3))
    # print(solution(110011, 10))
    s = "abcde"
    print(s[::-1])