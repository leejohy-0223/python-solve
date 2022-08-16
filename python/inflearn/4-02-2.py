from collections import defaultdict

str1 = input()
str2 = input()

maps = defaultdict(int)
for i in str1:
    maps[i] += 1

# 두번째 str2를 돌면서, 해당 키를 가지고 있는지 체크하고 기존에 올려둔 값을 1씩 내린다.
result = "YES"
for i in str2:
    if maps[i] == 0:
        result = "NO"
        break
    maps[i] -= 1
print(result)