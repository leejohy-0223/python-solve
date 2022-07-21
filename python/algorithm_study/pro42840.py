def solution(answers):
    arrays = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    result = [0 for _ in range(3)]
    answer_len = len(answers)
    for i in range(3):
        now = arrays[i]
        for j in range(0, answer_len, len(now)):
            tmp = answers[j:j + len(now)]

            for k in range(len(tmp)):
                if tmp[k] == now[k]:
                    result[i] += 1

    value = max(result)

    tmp_list = list()
    for i in range(3):
        if result[i] == value:
            tmp_list.append(i + 1)

    return tmp_list


if __name__ == '__main__':
    solution([1, 3, 2, 4, 2])
