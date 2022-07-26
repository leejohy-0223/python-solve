n = int(input())

record = []
for _ in range(n):
    name, score = input().split()
    record.append((name, int(score)))


record.sort(key=lambda student: student[1])

for r in record:
    print(r[0], end=' ')

