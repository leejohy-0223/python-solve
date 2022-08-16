from collections import defaultdict
strings = input()
target = input()

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for i in range(len(target)):
    dic1[strings[i]] += 1

for s in target:
    dic2[s] += 1

lt = 0
result = 1 if dic1 == dic2 else 0

for rt in range(len(target), len(strings)):
    # rt위치 추가
    dic1[strings[rt]] += 1

    # lt위치 제거
    dic1[strings[lt]] -= 1
    if dic1[strings[lt]] == 0:
        del dic1[strings[lt]]

    # 비교
    result += 1 if dic1 == dic2 else 0
    lt += 1

print(result)