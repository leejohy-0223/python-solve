def solution(stones, k):
    left = 0
    right = max(stones)

    while left < right:
        mid = (left + right) // 2
        cnt = 0

        for stone in stones:
            if stone - mid > 0:
                cnt = 0
                continue
            cnt += 1
            if cnt == k:
                break

        # cnt == k 또는 cnt > k라면 인원을 줄여야한다.
        if cnt >= k:
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))