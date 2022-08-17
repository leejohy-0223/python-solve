strings = input()


def solution():
    stack = list()
    for i in strings:
        if i == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()
    return "YES"

if __name__ == '__main__':
    print(solution())
