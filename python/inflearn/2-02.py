N = int(input())
students = list(map(int, input().split()))

max_height = students[0]
cnt = 1
for i in range(1, len(students)):
    if students[i] > max_height:
        cnt += 1
        max_height = students[i]

print(cnt)