def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()

        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)


if __name__ == '__main__':
    stk = [1, 2, 3]

    print(stk[:])
    print(stk[:0])
    print(stk[:-1])
    print(stk[:-2])
    print(stk[:-3])
