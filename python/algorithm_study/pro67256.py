def solution(numbers, hand):
    answer = ''
    keyMap = dict()
    keyMap[2], keyMap[5], keyMap[8], keyMap[0] = 0, 1, 2, 3

    board = [[0] for _ in range(4)]
    board[0] = [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4]
    board[1] = [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3]
    board[2] = [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2]
    board[3] = [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]

    # 초기 위치
    lPos, rPos = 10, 11
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            lPos = number
        elif number in [3, 6, 9]:
            answer += "R"
            rPos = number
        else:
            lDist = board[keyMap[number]][lPos]
            rDist = board[keyMap[number]][rPos]

            if lDist > rDist:
                answer += "R"
                rPos = number
            elif lDist < rDist:
                answer += "L"
                lPos = number
            else:
                if hand == "right":
                    answer += "R"
                    rPos = number
                else:
                    answer += "L"
                    lPos = number

    return answer


if __name__ == '__main__':
    # print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
