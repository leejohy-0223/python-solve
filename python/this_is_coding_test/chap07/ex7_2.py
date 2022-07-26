n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

# 절단기가 높아지면 떡이 덜 썰린다.
start = 0
end = max(rice_cake)

while start < end:

    mid = (start + end) // 2

    temp_sum = 0
    for i in rice_cake:
        if i > mid:
            temp_sum += (i - mid)

    # 떡이 더 썰렸으면 start를 올려 mid를 올린다.
    if m <= temp_sum:
        start = mid + 1
    else:
        end = mid

print(end - 1)
