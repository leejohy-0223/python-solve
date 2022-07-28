def solution(number, k):
    stack = [number[0]]
    for i in range(1, len(number)):
        while len(stack) > 0 and k > 0 and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1

        if k == 0:
            while i < len(number):
                stack.append(number[i])
                i += 1
            break
        else:
            stack.append(number[i])

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)


if __name__ == '__main__':
    # print(solution("3924", 2))
    # print(solution("1231234", 3))
    # print(solution("4177252841", 4))
    print(solution("332", 1))
