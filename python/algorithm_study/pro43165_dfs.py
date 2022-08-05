cnt = 0


def dfs(summation, cur, numbers, target):
    global cnt
    if cur == len(numbers):
        if summation == target:
            cnt += 1
        return

    dfs(summation + numbers[cur], cur + 1, numbers, target)
    dfs(summation - numbers[cur], cur + 1, numbers, target)


def solution(numbers, target):

    dfs(0, 0, numbers, target)
    return cnt

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
