input1 = input()

result = ""
for i in input1:
    if 97 <= ord(i) <= 122:
        result += chr(ord(i) - 32)
    else:
        result += chr(ord(i) + 32)

print(result)