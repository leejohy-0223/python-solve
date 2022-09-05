def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        break_set = set()
        # 부수는 위치 set에 넣기
        for i in range(m - 1):
            for j in range(n - 1):
                if not board[i][j]:
                    continue
                if same_check(board, i, j, board[i][j]):
                    break_set.add((i, j))
                    break_set.add((i + 1, j))
                    break_set.add((i, j + 1))
                    break_set.add((i + 1, j + 1))

        # 없어진거 counting & 공백 채우기
        if break_set:
            answer += len(break_set)
            for i, j in break_set:
                board[i][j] = []
        else:
            return answer

        # 리밸런싱(위에서 아래로 당기기)
        for j in range(n):
            tmpArr = []
            for i in range(m - 1, -1, -1):
                if board[i][j]:
                    tmpArr.append(board[i][j])

            # tmpArr을 통해 board[idx][j]위치에 새로 정렬된 배열 넣기
            idx = m - 1
            for tmp in tmpArr:
                board[idx][j] = tmp
                idx -= 1
            for i in range(idx + 1):
                board[i][j] = []


def same_check(board, i, j, now):
    return now == board[i][j + 1] and now == board[i + 1][j] and now == board[i + 1][j + 1]


if __name__ == '__main__':
    # print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
