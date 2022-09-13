from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


def solution(tasks):
    arr = sorted(tasks)
    count, idx = 0, 0
    while idx < len(arr):
        cur_value = arr[idx]
        interval_count = count_by_range(arr, cur_value, cur_value)

        if interval_count == 1:
            return -1

        if interval_count == 2 or interval_count == 3:
            count += 1
        elif interval_count % 3 == 2:
            count += (interval_count + 1) // 3
        elif interval_count % 3 == 1:
            count += (interval_count + 2) // 3
        else:
            count += interval_count // 3

        idx = bisect_right(arr, cur_value)

    return count

if __name__ == '__main__':
    # print(solution([1, 1, 2, 3, 3, 2, 2]))
    print(solution([1, 1, 2, 2]))
    print(solution([4, 1, 2, 2]))
