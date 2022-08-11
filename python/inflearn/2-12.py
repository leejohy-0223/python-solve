# 1번째 row(테스트)로부터 나올 수 있는 짝들 조합을 구한다.
# 그리고 그 다음 row를 돌면서, 각 조합에 대해 index위치를 통해 first < second 위치인 경우에만 다시 n_result에 튜플을 넣는다.
# 모든 테스트가 끝나면, 조합 중 모든 테스트를 만족하는 짝만 나오게 된다.

from itertools import combinations

n, m = map(int, input().split())

first_row = list(map(int, input().split()))
results = combinations(first_row, 2)

cnt = 0
for i in range(m - 1):
    now_row = list(map(int, input().split()))
    n_result = []
    for first, second in results:
        if now_row.index(first) < now_row.index(second):
            n_result.append((first, second))

    results = n_result

print(len(results))



