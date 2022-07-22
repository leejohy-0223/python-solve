from collections import deque

tmp = deque([[1, 2], [3, 4]])

tmp.appendleft([2, 3])

print(tmp[0])

if [3, 2] in tmp:
    print("3, 4 is here")