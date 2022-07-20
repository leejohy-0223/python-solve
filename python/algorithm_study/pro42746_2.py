import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크면 1 반환, t2가 크면 -1 반환,


def solution(numbers):

    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)

    answer = str(int(''.join(n)))
    return answer


if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))
