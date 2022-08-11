strings = input()

strings += " "
cnt = 0
nowChr = strings[0]
result = ""
for s in strings:
    if s == nowChr:
        cnt += 1
    else:
        if cnt > 1:
            result += str(nowChr) + str(cnt)
        else:
            result += str(nowChr)
        cnt = 1
        nowChr = s


print(result)