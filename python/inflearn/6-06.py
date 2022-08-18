n = int(input())
students = list(map(int, input().split()))
collect = sorted(students)
answer = []

for idx, number in enumerate(students):
    if collect[idx] != number:
        answer.append(idx + 1)

print(" ".join(map(str, answer)))

