def binary_search():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] > m:
            hi = mid - 1
        elif nums[mid] < m:
            lo = mid + 1
        else:
            return mid + 1

if __name__ == '__main__':
    print(binary_search())
