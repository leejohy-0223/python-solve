s = input()

result = 0
for i in s:
    if i.isdigit():
        result = (result * 10) + int(i)

print(result)