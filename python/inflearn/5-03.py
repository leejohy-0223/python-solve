def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    moves = list(map(int, input().split()))

    stack = []
    result = 0
    for move in moves:
        for i in range(N):
            if board[i][move - 1] == 0:
                continue
            if len(stack) != 0 and stack[-1] == board[i][move - 1]:
                result += 2
                stack.pop()
            else:
                stack.append(board[i][move - 1])
            board[i][move - 1] = 0
            break
    return result

if __name__ == '__main__':
    print(solution())