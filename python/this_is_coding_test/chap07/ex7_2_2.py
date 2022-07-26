n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

# 절단기가 높아지면 떡이 덜 썰린다.
start = 0
end = max(rice_cake)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rice_cake:
        if x > mid:
            total += (x - mid)

    # 떡 양이 부족하면 절단기 낮추기
    if total < m:
        end = mid - 1
    else:  # 떡 양이 같거나 많다면 절단기 높이기
        result = mid
        start = mid + 1

print(result)
