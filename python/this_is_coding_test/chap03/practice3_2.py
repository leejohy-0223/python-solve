s = input()

result = 1
for i in s:
    if i == '0' or i == '1':
        result += int(i)
    else:
        result *= int(i)

print(result)
