from collections import Counter

input1 = input()
findChar = input()

counter = Counter(input1)

print(counter[findChar.lower()] + counter[findChar.upper()])
