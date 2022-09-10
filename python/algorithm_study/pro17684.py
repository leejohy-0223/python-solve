def solution(msg):
    answer = []
    dictionary = dict()
    for i in range(0, 26):
        dictionary[chr(ord('A') + i)] = i + 1

    i, j, length = 0, 0, len(msg)
    idx = 27
    while i < length:
        while j < length:
            tmp = msg[i:j + 1]
            if tmp not in dictionary:
                dictionary[tmp] = idx
                break
            j += 1
        answer.append(dictionary[msg[i:j]])
        idx += 1
        i = j

    return answer


if __name__ == '__main__':
    # print(solution("KAKAO"))
    print(solution("ABABABABABABABAB"))