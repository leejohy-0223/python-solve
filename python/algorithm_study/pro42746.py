def solution(numbers):

    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)

    # 각 자리수가 1000 이하,
    # * 2 라면 :  9, 991 -> 99 vs 991991 -> 3번째 자리 비교하려니 99는 끝났으므로 991이 이긴다.
    # * 3 이라면 : 9, 991 -> 999 vs 991991991 -> 3번째 자리 비교하니 999가 더 크므로 9가 이긴다.

    for i in numbers:
        answer += str(i)

    return str(int(answer))

if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))
