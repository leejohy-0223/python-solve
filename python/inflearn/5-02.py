def solution():
    strings = input()
    stack = []
    result = ""
    for i in strings:
        if i == "(":
            stack.append(1)
        elif i == ")":
            stack.pop()
        elif len(stack) == 0:
            result += i

    return result

if __name__ == '__main__':
    print(solution())
