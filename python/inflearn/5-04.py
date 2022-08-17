def solution():
    strings = input()
    stack = []
    for i in strings:
        if i.isdigit():
            stack.append(i)
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(str(eval(n2 + i + n1)))

    return stack[0]

if __name__ == '__main__':
    print(solution())