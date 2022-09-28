import math

n = int(input())

results = [0] * 50001

for i in range(1, 224):
    results[i ** 2] = 1

for i in range(2, n + 1):
    if results[i] != 1:
        tmp = 5
        for j in range(1, int(math.sqrt(i)) + 1):
            tmp = min(tmp, results[i - (j ** 2)])
        results[i] = tmp + 1

print(results[n])