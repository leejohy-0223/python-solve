s = input()

result = ""
for idx, c in enumerate(s):
    if idx == s.index(c):
        result += c

print(result)