# quick sort

arr = [7, 5, 9, 0, 1, 3, 1, 6, 2, 4, 8, 4]


def quick_sort(array):
    #  리스트가 하나 이하의 원소만 갖는다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(arr))
