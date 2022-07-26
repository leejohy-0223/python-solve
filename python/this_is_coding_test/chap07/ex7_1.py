import sys
from bisect import bisect

input = sys.stdin.readline

n = int(input())
part_list = sorted(list(map(int, input().split())))
m = int(input())
find_list = list(map(int, input().split()))

for i in find_list:
    # bisect는 같은 값이라면 해당 인덱스의 다음 인덱스를, 작은 값이라면 해당 인덱스의 위치를 반환한다.
    print("yes" if part_list[bisect(part_list, i) - 1] == i else "no", end=' ')

# 2, 3, 7, 8, 9 에서
# 5, 7, 9를 찾을 때
# 2, 3, 5가 반환된다.