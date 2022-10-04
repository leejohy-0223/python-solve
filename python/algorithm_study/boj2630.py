wCount, bCount = 0, 0


def sameCheck(sx, sy, n, arrs):
    first_value = arrs[sx][sy]
    for i in range(sx, sx + n):
        for j in range(sy, sy + n):
            if arrs[i][j] != first_value:
                return False
    return True


def solution(n, arrs, sx, sy):
    global wCount, bCount

    # check if all area is same
    chk = False
    if not sameCheck(sx, sy, n, arrs):
        # recursive
        chk = True
        solution(n // 2, arrs, sx, sy)
        solution(n // 2, arrs, sx, sy + (n // 2))
        solution(n // 2, arrs, sx + (n // 2), sy)
        solution(n // 2, arrs, sx + (n // 2), sy + (n // 2))

    if not chk:
        if arrs[sx][sy] == 0:
            wCount += 1
        else:
            bCount += 1

if __name__ == '__main__':
    n = int(input())
    arrs = [list(map(int, input().split())) for _ in range(n)]

    solution(n, arrs, 0, 0)
    print(str(wCount) + "\n" + str(bCount))
