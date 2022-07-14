n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
list.sort(arr)

first = arr[-1]
second = arr[-2]

remainder = m % k
result = (second * remainder) + (first * (m - remainder))
print(result)