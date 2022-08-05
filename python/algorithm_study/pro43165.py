from itertools import product

def solution(numbers, target):
    operation = ['+', '-']

    result = list(product(operation, repeat=len(numbers)))

    count = 0
    for r in result:
        result = 0
        for i in range(len(numbers)):
            if r[i] == '+':
                result += numbers[i]
            else:
                result -= numbers[i]
        if result == target:
            count += 1

    return count

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
