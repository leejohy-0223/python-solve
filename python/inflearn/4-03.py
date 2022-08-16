from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))

keys = defaultdict(int)
for i in nums[0:k]:
    keys[i] += 1

result = str(len(keys)) + " "
lt = 0
for rt in range(k, n):
    # rt 위치 추가
    keys[nums[rt]] += 1

    # lt 위치 제거
    keys[nums[lt]] -= 1

    # lt 위치 값이 더이상 없다면, 키 목록에서 제거
    if keys[nums[lt]] == 0:
        del keys[nums[lt]]

    # 길이 갱신
    result += str(len(keys)) + " "
    lt += 1

print(result)

