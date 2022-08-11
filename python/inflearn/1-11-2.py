# 맨 뒤에도 포함시켜야 할 경우, 마지막에 빈 문자열을 추가해도 좋은 방법이다.

strings = input()

strings += " "
cnt = 1
result = ""

for i in range(0, len(strings) - 1):
    if strings[i] == strings[i + 1]:
        cnt += 1
    else:
        result += strings[i]
        if cnt > 1:
            result += str(cnt)
            cnt = 1

print(result)