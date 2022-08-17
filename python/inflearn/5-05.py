def solution():
    strings = input()
    stack = []

    result = 0
    for s in range(len(strings)):
        # 닫는 괄호면서
        if strings[s] == ')':
            # 레이져라면 레이져 몸통 날리고 개수 더하기
            if strings[s - 1] == '(':
                stack.pop()
                result += len(stack)
            # 레이져가 아니라면 쇠막대기 날리기
            else:
                result += 1
                stack.pop()
        # 여는 괄호라면 무조건 넣기
        else:
            stack.append('(')

    return result

if __name__ == '__main__':
    print(solution())