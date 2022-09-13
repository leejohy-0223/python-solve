def solution(s):
    check = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

    for i in check:
        if str(s).find(i) != -1:
            if i == "000":
                return 0
            else:
                return i

    return -1


if __name__ == '__main__':
    print(solution("12223"))