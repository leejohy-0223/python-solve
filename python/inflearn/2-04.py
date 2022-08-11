N = int(input())

fibo = [1, 1]
for i in range(2, N):
    fibo.append(fibo[i - 2] + fibo[i - 1])

print(" ".join(map(str, fibo)))