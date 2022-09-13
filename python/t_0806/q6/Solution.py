def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = dict()

    calculate(answer, names_one, steps_one)
    calculate(answer, names_two, steps_two)
    calculate(answer, names_three, steps_three)

    sorted_dict = sorted(answer.items(), key=lambda x: (x[1], x[0]), reverse=True)  # 이름은 reverse 반대로,,짜식아

    result = []
    for i in sorted_dict:
        result.append(i[0])

    return result


def calculate(answer, names_one, steps_one):
    nMap = dict()
    for step, name in zip(steps_one, names_one):
        if name in nMap:
            nMap[name] = max(nMap[name], step)
        else:
            nMap[name] = step
    # 기존 내용에 더하기
    for key, value in nMap.items():
        if key in answer:
            answer[key] += value
        else:
            answer[key] = value


if __name__ == '__main__':
    print(solution([1, 2, 3, 5, 5], ["james", "bob", "alice", "cca", "aa"], [10, 20, 30, 5, 5], ["james", "alice", "bob", "aa", "cca"], [1000, 1, 1, 2000], ["bob", "alice", "james", "bob"]))
