# 효율성 시간 초과

def solution(n, k, cmd):
    result = ['O'] * n
    curPos = k
    removeStack = []
    for command in cmd:
        if command == "C":
            result[curPos] = 'X'
            removeStack.append(curPos)

            tmpCurPos = curPos + 1
            # 먼저 아래로 이동
            while tmpCurPos < n:
                if result[tmpCurPos] == 'O':
                    curPos = tmpCurPos
                    break
                tmpCurPos += 1

            # 맨 아래까지 갔었다면, 위로 이동
            if tmpCurPos == n:
                tmpCurPos = curPos - 1
                while tmpCurPos >= 0:
                    if result[tmpCurPos] == 'O':
                        curPos = tmpCurPos
                        break
                    tmpCurPos -= 1

            # 맨 위에도 없다면 0으로 초기화
            if tmpCurPos == -1:
                curPos = 0
            continue
        if command == "Z":
            # 제일 최근에 지운 것 복구
            result[removeStack.pop()] = 'O'
            continue

        direction, amount = command.split(" ")
        amount = int(amount)
        moveCount = 0
        if direction == 'U':
            tmpPos = curPos - 1
            while moveCount != amount:
                if result[tmpPos] == 'O':
                    moveCount += 1
                tmpPos -= 1
            curPos = tmpPos + 1
        else:
            tmpPos = curPos + 1
            while moveCount != amount:
                if result[tmpPos] == 'O':
                    moveCount += 1
                tmpPos += 1
            curPos = tmpPos - 1

    return "".join(result)


if __name__ == '__main__':
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
