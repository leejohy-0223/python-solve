# https://www.acmicpc.net/problem/6064
# x를 기준으로, x만큼 값을 올리고 해당 값으로부터 tmpY를 계산한다. tmpY가 y(target)와 같을 경우 누적된 x의 값을 반환한다.
# set에 tmpY가 존재한다는 말은 동일한 나머지가 반복된다는 것을 의미하며, 계산할 수 없다는 것을 의미하므로 -1을 반환한다.

import sys

t = int(input())

result = ""
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    results = x
    tmpY = x % n

    if tmpY == 0:
        tmpY = n

    chk = set()
    while True:
        if y == tmpY:
            result += (str(results) + "\n")
            break
        tmpY = (tmpY + m) % n
        if tmpY == 0:
            tmpY = n
        if tmpY in chk:
            result += (str(-1) + "\n")
            break
        chk.add(tmpY)
        results += m

print(result)