from collections import defaultdict


def solution(info, query):
    answer = []
    table = defaultdict(list)
    for i in info:
        language, stack, career, food, score = i.split(" ")
        table[(language, stack, career, food)].append(int(score))

    for key in table:
        table[key].sort()

    for q in query:
        q = q.replace(" and ", " ")
        tmpKey = []
        for tmp in q.split(" "):
            if tmp != '-':
                tmpKey.append(tmp)

        targetScore = int(tmpKey[-1])
        tmpKey = set(tmpKey[:-1])

        count = 0
        for key in table:
            keySet = set(key)
            if not (tmpKey - keySet):
                scoreBoard = table[key]
                start, end = 0, len(scoreBoard)
                # 하한 찾기, 즉 만족하지 못한 위치까지 start를 이동
                while start < end:
                    mid = (start + end) // 2
                    if scoreBoard[mid] >= targetScore:
                        end = mid
                    else:
                        start = mid + 1
                # 최종적으로 start는 조건을 만족하는 가장 작은 인덱스를 가리킴
                count += len(scoreBoard) - start

        answer.append(count)

    return answer


if __name__ == '__main__':
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
