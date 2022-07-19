import sys
from bisect import bisect

sys.setrecursionlimit(10 ** 6)


def post_order(s, e):
    if s == e:
        return

    d = pre_order[s]
    idx = bisect(pre_order, d, s, e)

    post_order(s + 1, idx)
    post_order(idx, e)
    print(d)


pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))

    except:
        break

post_order(0, len(pre_order))
