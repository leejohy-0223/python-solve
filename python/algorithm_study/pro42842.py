import math

def solution(brown, yellow):

    if yellow == 1:
        sqrt = int(math.sqrt(brown + yellow))
        return [sqrt, sqrt]

    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            brown_w = (yellow // i) + 1
            brown_l = i + 1
            if (brown_w + brown_l) * 2 == brown:
                return [brown_w + 1, brown_l + 1]


if __name__ == '__main__':
    print(solution(8, 1))