# 이진 탐색 소스코드 구현(반복)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n, tar = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, tar, 0, n - 1)

if result is None:
    print("원소가 존재하지 않습니다.")

else:
    print(result + 1)