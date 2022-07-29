from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 모든 단어를 길이마다 나누어 저장하기 위한 리스트
array = [[] for _ in range(10001)]

# 모든 단어를 길이마다 나누어 뒤집어서 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)  # 단어를 정방향으로 삽입
        reversed_array[len(word)].append(word[::-1])  # 단어를 역방향으로 삽입

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    # 쿼리를 하나씩 확인하며 처리
    for query in queries:
        # 접미사에 와일드카드가 붙은 경우
        if query.endswith('?'):
            answer.append(count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
        # 접두사에 붙은 경우
        else:
            answer.append(count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))

    return answer


if __name__ == '__main__':
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                   ["fro??", "????o", "fr???", "fro???", "pro?"]))

    # o???? -> oaaaa ~ ozzzz -> oakak, okopd
