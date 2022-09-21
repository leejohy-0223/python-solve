def solution(n, k, cmd):
    deleteStack = []
    pos, size = k, n
    for command in cmd:
        if command == 'C':
            deleteStack.append(pos)
            size -= 1
            if pos == size:
                pos -= 1
            continue
        if command == 'Z':
            if pos >= deleteStack.pop():
                pos += 1
            size += 1
            continue

        direction, value = command.split(" ")
        if direction == 'U':
            pos -= int(value)
        else:
            pos += int(value)

    results = ['O'] * size

    while deleteStack:
        now = deleteStack.pop()
        results.insert(now, 'X')

    return "".join(results)


if __name__ == '__main__':
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

    # tmp = [1, 2, 3]
    # print(tmp[:2] + [10] + tmp[2:])
