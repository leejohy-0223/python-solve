def solution(N, number):
    sum_set = [set() for _ in range(9)]  # set 8개 만들기(1 ~ 8 사용)

    for i in range(1, 9):
        n_set = {int(str(N) * i)}

        for j in range(1, i // 2 + 1):
            for op1 in sum_set[j]:
                for op2 in sum_set[i - j]:
                    n_set.add(op1 + op2)
                    n_set.add(op1 - op2)
                    n_set.add(op2 - op1)
                    n_set.add(op1 * op2)
                    if op1 != 0:
                        n_set.add(op2 // op1)
                    if op2 != 0:
                        n_set.add(op1 // op2)

        sum_set[i] = n_set
        if number in sum_set[i]:
            return i

    return -1


if __name__ == '__main__':
    print(solution(2, 11))
