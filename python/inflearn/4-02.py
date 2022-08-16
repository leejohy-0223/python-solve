from collections import Counter

str1 = input()
str2 = input()

c1 = sorted(Counter(str1).most_common())
c2 = sorted(Counter(str2).most_common())

if c1 == c2:
    print("YES")
else:
    print("NO")