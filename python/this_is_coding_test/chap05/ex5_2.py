def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):

    # n <= 1일 때만 여기서 탈출하고
    if n <= 1:
        return 1

    # 나머지는 여기서 탈출한다.
    return n * factorial_recursive(n - 1)


