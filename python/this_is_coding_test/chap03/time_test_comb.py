import operator as op
from functools import reduce
from itertools import combinations
import time

data = ['A', 'B', 'C', 'D', 'Ef', 'gdf', 'dfs', 'dsf', 'sdf', 'sdfds', 'sdf', 'dsfs', 'sdf', ' adsf', 'adsfas', 'dfa',
        'adf', 'adadsg', 'asdf', 'adfs',
        'A', 'B', 'C', 'D', 'Ef', 'gdf', 'dfs', 'dsf', 'sdf', 'sdfds', 'sdf', 'dsfs', 'sdf', ' adsf', 'adsfas', 'dfa',
        'adf', 'adadsg', 'asdf', 'adfs',
        'A', 'B', 'C', 'D', 'Ef', 'gdf', 'dfs', 'dsf', 'sdf', 'sdfds', 'sdf', 'dsfs', 'sdf', ' adsf', 'adsfas', 'dfa',
        'adf', 'adadsg', 'asdf', 'adfs',
        'A', 'B', 'C', 'D', 'Ef', 'gdf', 'dfs', 'dsf', 'sdf', 'sdfds', 'sdf', 'dsfs', 'sdf', ' adsf', 'adsfas', 'dfa',
        'adf', 'adadsg', 'asdf', 'adfs',
        'A', 'B', 'C', 'D', 'Ef', 'gdf', 'dfs', 'dsf', 'sdf', 'sdfds', 'sdf', 'dsfs', 'sdf', ' adsf', 'adsfas', 'dfa',
        'adf', 'adadsg', 'asdf', 'adfs']

start_time = time.time()
result = len(list(combinations(data, 2)))
end_time = time.time()

r1_time = end_time - start_time
print(r1_time)
print(result, end='\n')


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError

    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator // denominator


start_time = time.time()
r2 = nCr(100, 2)
end_time = time.time()

r2_time = end_time - start_time

print(r2)
print(r2_time)
print(r1_time // r2_time)
