import copy


def rotateKey(key):
    n = len(key)
    tmpKey = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmpKey[j][n - i - 1] = key[i][j]
    return tmpKey


def solution(key, lock):
    # expand Lock
    nSize = len(lock) + 2 * (len(key) - 1)
    nLock = [[0] * nSize for _ in range(nSize)]
    keyLen = len(key)

    # insert existing lock
    for i in range(len(lock)):
        for j in range(len(lock)):
            nLock[i + keyLen - 1][j + keyLen - 1] = lock[i][j]

    # rotate & check
    for _ in range(4):
        key = rotateKey(key)
        for i in range(len(lock) + keyLen - 1):
            for j in range(len(lock) + keyLen - 1):
                tmpLock = copy.deepcopy(nLock)

                # union key and lock
                for k in range(keyLen):
                    for l in range(keyLen):
                        tmpLock[i + k][j + l] += key[k][l]

                # check if all values are '1'
                allPass = True
                for k in range(keyLen - 1, keyLen - 1 + len(lock)):
                    for l in range(keyLen - 1, keyLen - 1 + len(lock)):
                        if tmpLock[k][l] != 1:
                            allPass = False
                            break
                    if not allPass:
                        break
                if allPass:
                    return True

    return False

if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
