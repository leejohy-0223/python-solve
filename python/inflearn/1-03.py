input1 = input()

mLength = 0
result = ""
while " " in input1:
    idx = input1.index(" ")
    tmp = input1[0:idx]
    if mLength < len(tmp):
        mLength = len(tmp)
        result = tmp
    input1 = input1[idx + 1:]

print(result) if mLength >= len(input1) else print(input1)
