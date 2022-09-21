# 링크드리스트로 구현

class Node:
    def __init__(self, left=None, right=None):
        self.remove = False
        self.left = left
        self.right = right


def solution(n, k, cmd):
    # init linked list
    board = [Node(i - 1, i + 1) for i in range(n)]
    board[0].left = None
    board[-1].right = None
    deleteInfo = []
    cursor = k
    for command in cmd:
        if command[0] == 'U':
            pos, move = command.split()
            for _ in range(int(move)):
                cursor = board[cursor].left
        elif command[0] == 'D':
            pos, move = command.split()
            for _ in range(int(move)):
                cursor = board[cursor].right
        elif command[0] == 'C':
            deleteInfo.append(cursor)
            board[cursor].remove = True

            l, r = board[cursor].left, board[cursor].right

            if l is not None:  # check if l is not None or 0, because '0' case also must check
                board[l].right = r

            if r:
                board[r].left = l
                cursor = r  # 커서를 오른쪽으로 이동
            else:
                cursor = l  # 마지막 행이라면 l로 커서 변경
        else:
            recover = deleteInfo.pop()
            board[recover].remove = False

            l, r = board[recover].left, board[recover].right

            if l:
                board[l].right = recover
            if r:
                board[r].left = recover

    return "".join('O' if not node.remove else 'X' for node in board)



if __name__ == '__main__':
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

    # tmp = [1, 2, 3]
    # print(tmp[:2] + [10] + tmp[2:])
