import operator as op
from functools import reduce


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError

    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator // denominator


a, b = map(int, input().split())
ball = list(map(int, input().split()))

array = [0] * 11

for i in ball:
    array[i] += 1

result = nCr(a, 2)

for i in array:
    if i > 1:
        result -= nCr(i, 2)

print(result)
