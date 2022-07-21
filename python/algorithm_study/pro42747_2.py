def solution(citations):
    sorted_citations = sorted(citations, reverse=True)

    for idx in range(len(sorted_citations)):
        if idx >= sorted_citations[idx]:
            return idx

    return len(sorted_citations)


if __name__ == '__main__':
    print(solution([2, 2, 2, 2, 6, 6, 6, 6]))