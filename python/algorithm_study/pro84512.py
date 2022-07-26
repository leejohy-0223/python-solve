multi_template = [
    781, 156, 31, 6, 1
]

value_map = dict()

value_map['A'] = 0
value_map['E'] = 1
value_map['I'] = 2
value_map['O'] = 3
value_map['U'] = 4


def solution(word):
    result = 0
    for i in range(len(word)):
        result += (1 + (multi_template[i] * value_map[word[i]]))

    return result


if __name__ == '__main__':
    print(solution("EIO"))