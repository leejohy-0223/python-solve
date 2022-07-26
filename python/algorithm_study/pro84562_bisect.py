from bisect import bisect_left
from itertools import product

CHARACTER = "AEIOU"
MAX_LENGTH = 5

dictionary = sorted(
    "".join(p) for i in range(1, MAX_LENGTH + 1) for p in product(CHARACTER, repeat=i)
)


def solution(word):
    print(dictionary)
    return bisect_left(dictionary, word)


if __name__ == '__main__':
    print(solution("A"))