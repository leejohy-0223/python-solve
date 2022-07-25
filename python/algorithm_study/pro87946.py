from itertools import permutations

def solution(k, dungeons):
    result = 0
    for orders in list(permutations(dungeons)):
        init = k
        tmp = 0
        for order in orders:
            #  최소 피로도인지 확인
            if order[0] <= init:
                init -= order[1]
                tmp += 1
            else:
                break
        result = max(result, tmp)

    return result

if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))