import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = sys.maxsize

class Position:
    def __init__(self, bX, bY, fee, dir):
        self.bX = bX
        self.bY = bY
        self.fee = fee
        self.dir = dir


def solution(board):
    length = len(board)
    answerBoard = [[[INF] * length for _ in range(length)] for _ in range(4)]

    q = deque([])
    q.append(Position(0, 0, 0, 0))
    q.append(Position(0, 0, 0, 1))

    while q:
        now = q.popleft()
        if now.bX == length - 1 and now.bY == length - 1:
            continue
        for i in range(4):
            nx = dx[i] + now.bX
            ny = dy[i] + now.bY
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                tmpFee = now.fee + 100 if (now.dir == -1 or now.dir == i) else now.fee + 600
                if answerBoard[i][nx][ny] > tmpFee:
                    answerBoard[i][nx][ny] = tmpFee
                    q.append(Position(nx, ny, tmpFee, i))

    answer = INF
    for i in range(4):
        answer = min(answer, answerBoard[i][-1][-1])
    return answer


if __name__ == '__main__':
    # print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    # print(solution(
    #     [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
    #      [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
    # print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
    #                 [0, 0, 0, 0, 0, 0]]))
