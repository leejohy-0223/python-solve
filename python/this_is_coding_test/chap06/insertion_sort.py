# insertion sort : 거의 정렬되어있는 경우 유리하다. 그럴 경우 break에서 금방 빠져나오게 된다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 이미 맨 앞은 정렬되어있다고 가정하고 0번째가 아닌 1번째부터 시작
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
