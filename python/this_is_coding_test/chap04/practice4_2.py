s = input()

summation = 0
tmp = list()
for i in s:
    if i.isdigit():
        summation += int(i)
        continue
    tmp.append(i)

result = sorted(tmp)
print(''.join(result), summation, sep='')