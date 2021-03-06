def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(sorted(array[i - 1: j])[k - 1])

    return result

if __name__ == '__main__':
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])