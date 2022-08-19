# DFS 탈출 조건에 summation - tSum + subTotal < maximum을 통해 시간초과를 해결한다.
# 즉, 아직 안더해질 목록들(summation - tSum)과 subTotal(지금까지 더해진 값)이 maximum보다 작다면 더 더해서 비교핦 필요가 없으므로 추가 필요

import sys


def DFS(L, subTotal, tSum):
    global maximum
    if subTotal > c or summation - tSum + subTotal < maximum:
        return
    if L == n:
        maximum = max(maximum, subTotal)
    else:
        DFS(L + 1, subTotal + a[L], tSum + a[L])
        DFS(L + 1, subTotal, tSum + a[L])

c, n = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
maximum = 0
summation = sum(a)
DFS(0, 0, 0)
print(maximum)
