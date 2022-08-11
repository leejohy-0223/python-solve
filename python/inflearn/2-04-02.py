N = int(input())

a, b = 1, 1
result = "1 1 "
for i in range(2, N):
    c = a + b
    result += str(c) + " "
    a, b = b, c

print(result)
