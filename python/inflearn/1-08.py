import re

s = input()
result = re.sub("[^A-Z]", "", s.upper())

lt, rt = 0, len(result) - 1
while lt < rt:
    if result[lt] != result[rt]:
        print("NO")
        break
    lt += 1
    rt -= 1

else:
    print("YES")