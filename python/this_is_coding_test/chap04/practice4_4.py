def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


def solution(key, lock):
    keyLen = len(key)
    nSize = (keyLen - 1) * 2 + len(lock)
    nBoard = [[0] * nSize for _ in range(nSize)]

    # 실제 자물쇠를 집어 넣기
    for i in range(keyLen - 1, keyLen - 1 + len(lock)):
        for j in range(keyLen - 1, keyLen - 1 + len(lock)):
            nBoard[i][j] = lock[i - (keyLen - 1)][j - (keyLen - 1)]

    # 열쇠 돌리며 체크하기
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for i in range(len(lock) + keyLen - 1):
            for j in range(len(lock) + keyLen - 1):
                # 열쇠 꼽기
                match_result = put_key_and_check(i, j, key, keyLen, lock, nBoard)

                if match_result:
                    return True

                # 열쇠 빼기
                for k in range(i, i + keyLen):
                    for l in range(j, j + keyLen):
                        nBoard[k][l] -= key[k - i][l - j]

    return False


def put_key_and_check(i, j, key, keyLen, lock, nBoard):
    for k in range(i, i + keyLen):
        for l in range(j, j + keyLen):
            nBoard[k][l] += key[k - i][l - j]
    # 자물쇠 체크
    match_result = check_match(keyLen, lock, nBoard)
    return match_result


def check_match(keyLen, lock, nBoard):
    for k in range(keyLen - 1, keyLen - 1 + len(lock)):
        for l in range(keyLen - 1, keyLen - 1 + len(lock)):
            if nBoard[k][l] != 1:
                return False
    return True


if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
