# h_index는 h번 이상 인용된 논문이 h편 이상임을 기준으로 한다. 문제를 제대로 읽자(h번 이하 인용된 논문이 h편 이하일 필요는 없다.)

def solution(citations):
    citations = sorted(citations)
    h_index = 0
    cit_len = len(citations)

    while True:
        chk = False
        for idx in range(cit_len):
            if citations[idx] < h_index:
                continue

            moreThan = cit_len - idx
            if moreThan >= h_index:
                h_index += 1
                chk = True
                break
            else:
                return h_index - 1

        if not chk:
            return h_index - 1


if __name__ == '__main__':
    print(solution([2, 2, 2, 2, 5, 5, 6, 6]))
