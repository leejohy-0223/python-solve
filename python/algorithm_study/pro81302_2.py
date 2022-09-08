def check(place):
    for idxRow, row in enumerate(place):
        for idxCol, cel in enumerate(row):
            if cel != 'P':
                continue
            if idxRow + 1 < 5 and place[idxRow + 1][idxCol] == 'P':
                return 0
            if idxCol + 1 < 5 and place[idxRow][idxCol + 1] == 'P':
                return 0
            if idxRow + 2 < 5 and place[idxRow + 2][idxCol] == 'P' and place[idxRow + 1][idxCol] != 'X':
                return 0
            if idxCol + 2 < 5 and place[idxRow][idxCol + 2] == 'P' and place[idxRow][idxCol + 1] != 'X':
                return 0
            if idxRow + 1 < 5 and idxCol + 1 < 5 and place[idxRow + 1][idxCol + 1] == 'P' and (place[idxRow + 1][idxCol] != 'X' or place[idxRow][idxCol + 1] != 'X'):
                return 0
            if idxRow - 1 >= 0 and idxCol + 1 < 5 and place[idxRow - 1][idxCol + 1] == 'P' and (place[idxRow - 1][idxCol] != 'X' or place[idxRow][idxCol + 1] != 'X'):
                return 0
    return 1


def solution(places):
    return [check(place) for place in places]



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
