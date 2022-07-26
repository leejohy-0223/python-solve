# 이진 탐색 소스 코드 구현
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


n, tar = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, tar, 0, n - 1)

if result is None:
    print("원소가 존재하지 않습니다.")

else:
    print(result + 1)
