def solution(record):
    answer = []
    idDicts = dict()

    for r in record:
        split_result = r.split(" ")
        # enter, change 동작
        if len(split_result) == 3:
            idDicts[split_result[1]] = split_result[2]

    for r in record:
        split_result = r.split(" ")
        # Enter일 경우
        if split_result[0] == "Enter":
            answer.append(idDicts[split_result[1]] + "님이 들어왔습니다.")
        elif split_result[0] == "Leave":
            answer.append(idDicts[split_result[1]] + "님이 나갔습니다.")

    return answer


if __name__ == '__main__':
    print(solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
