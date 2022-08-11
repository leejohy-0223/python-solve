from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    if begin == words:
        return 0

    q = deque([begin])
    chk = [False] * len(words)
    length = len(target)

    depth = 0
    while q:
        size = len(q)
        for _ in range(size):
            now = q.popleft()
            # 모든 단어 탐색
            if now == target:
                return depth
            for i in range(len(words)):
                # 이전에 탐색된 단어라면 pass
                if chk[i]:
                    continue

                comparisonTarget = words[i]
                cnt = 0
                for c, w in zip(now, comparisonTarget):
                    if c == w:
                        cnt += 1

                # 하나만 다르다면, 큐에 넣기
                if cnt == length - 1:
                    q.append(comparisonTarget)
                    chk[i] = True

        depth += 1
    return 0

if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
