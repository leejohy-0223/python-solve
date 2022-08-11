N = int(input())
stuMap = []

for i in range(N):
    stuMap.append(list(map(int, input().split())))

maxResult = 0
resultList = []
for i in range(N):
    student = stuMap[i]
    countSet = set()

    for j in range(N):
        compareStu = stuMap[j]
        for k in range(5):
            if student[k] == compareStu[k]:
                countSet.add(j)
                break

    if maxResult < len(countSet):
        maxResult = len(countSet)
        resultList = [i]
    elif maxResult == len(countSet):
        resultList.append(i)

print(sorted(resultList)[0] + 1)