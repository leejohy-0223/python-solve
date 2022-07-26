arr = [7, 5, 9, 0, 1, 3, 1, 6, 2, 4, 8, 4]


def quick_sort(array):
    #  리스트가 하나 이하의 원소만 담고 있다면 바로 반환
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    left_array = [x for x in tail if x <= pivot]
    right_array = [x for x in tail if x > pivot]

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


print(quick_sort(arr))