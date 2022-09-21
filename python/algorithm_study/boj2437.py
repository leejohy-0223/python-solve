# 새로운 값은 maxValue(타겟 값) - 1에 해당하는 값까지 감당이 가능하다. 따라서 maxValue에 value를 더해서 매번 갱신한다.

n = int(input())
m = list(map(int, input().split()))

maxValue = 1
m.sort()

for value in m:
    if value <= maxValue:
        maxValue += value
    else:
        print(maxValue)
        break

print(maxValue)