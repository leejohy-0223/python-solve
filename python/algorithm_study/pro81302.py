def solution(places):
    answer = []
    for place in places:
        board = []
        for p in place:
            board.append(list(p))

        people_pos = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    people_pos.append((i, j))

        chk = False
        while people_pos:
            ni, nj = people_pos.pop(0)
            if (ni + 1 < 5 and board[ni + 1][nj] == 'P') or (nj + 1 < 5 and board[ni][nj + 1] == 'P'):
                chk = True
                break

            if ni + 2 < 5 and board[ni + 2][nj] == 'P':
                if board[ni + 1][nj] != 'X':
                    chk = True
                    break

            if nj + 2 < 5 and board[ni][nj + 2] == 'P':
                if board[ni][nj + 1] != 'X':
                    chk = True
                    break

            if ni + 1 < 5 and nj + 1 < 5 and board[ni + 1][nj + 1] == 'P':
                if not (board[ni + 1][nj] == 'X' and board[ni][nj + 1] == 'X'):
                    chk = True
                    break

            if ni - 1 >= 0 and nj + 1 < 5 and board[ni - 1][nj + 1] == 'P':
                if not (board[ni - 1][nj] == 'X' and board[ni][nj + 1] == 'X'):
                    chk = True
                    break

        if not chk:
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == '__main__':
    # print(solution([
    #     ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    #     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    #     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    #     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    #     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
    print(solution([
        ["OOOOO", "OOOOO", "OOOOO", "OPOOO", "POOOO"],
        ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"],
        ["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"],
        ["PXOOO", "XPOOO", "OOOOO", "OOOOO", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
