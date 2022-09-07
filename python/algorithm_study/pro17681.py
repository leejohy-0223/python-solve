def solution(n, arr1, arr2):
    answer = []
    template = '{0:0' + str(n) + 'b}'
    for a1 in arr1:
        answer.append(template.format(a1))

    idx = 0
    for a2 in arr2:
        tmp2 = template.format(a2)
        before = answer[idx]
        tmpResult = ""
        for i in range(n):
            if tmp2[i] == before[i] == "0":
                tmpResult += " "
            else:
                tmpResult += "#"
        answer[idx] = tmpResult
        idx += 1

    return answer


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
