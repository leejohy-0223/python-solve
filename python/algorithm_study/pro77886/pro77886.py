def solution(s):
    answers = []
    chkTemplate = ["1", "1"]

    for strings in s:
        stack = []
        count_110 = 0
        for chr in strings:
            if stack[-2:] == chkTemplate and chr == "0":
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(chr)

        # find first index that is not zero
        count_1 = 0
        for idx in range(len(stack) - 1, -1, -1):
            if stack[idx] == '0':
                break
            count_1 += 1

        # count_1 means 1이 끝나는 곳
        answer = "".join(stack[:len(stack) - count_1]) + "110" * count_110 + "1" * count_1
        answers.append(answer)

    return answers


if __name__ == '__main__':
    print(solution(["1110", "100111100", "0111111010"]))
    # stk = [1, 2, 3, 4, 5, 6, 7]
    # print(stk[-3:])
    # stk = stk[:-3]
    # print(stk)
