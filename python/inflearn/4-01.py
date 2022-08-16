from collections import Counter

n = int(input())
strings = input()
result = Counter(strings).most_common(1)[0][0]

print(result)
