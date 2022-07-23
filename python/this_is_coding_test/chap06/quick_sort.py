# quick sort

arr = [7, 5, 9, 0, 1, 3, 1, 6, 2, 4, 8, 4]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 데이터를 찾는다.(작으면 while 빠져나온다.)
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot보다 작은 데이터를 찾는다.(크면 while 빠져나온다.)
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 pivot과 right(엇갈려서 더 작아짐) 변경
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # 아니라면 left, right 변경
        else:
            array[left], array[right] = array[right], array[left]

    # right에는 최종적으로 찾아진 위치의 값이 들어있다. 원래 pivot에 있던 값의 정확한 위치가 교차되어 찾아진 위치가 되는 것이다.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
