import math
from itertools import permutations

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        result = list(map(int, map(''.join, permutations(numbers, i))))
        for num in result:
            if is_prime_num(num):
                answer.add(num)
    return len(answer)


def is_prime_num(n):
    if n in (0, 1):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(solution("011"))
