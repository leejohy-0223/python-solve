def solution(s):
    if len(s) == 1:
        return 1
    length = len(s) // 2
    answer = 1000
    for i in range(1, length + 1):
        start = s[0:i]
        count = 1
        result, nxt = "", ""
        for j in range(i, len(s), i):
            nxt = s[j:j+i]
            if start == nxt:
                count += 1
            else:
                result += str(count) + start if count > 1 else start
                count = 1
                start = nxt

        result += str(count) + nxt if count > 1 else nxt
        answer = min(answer, len(result))

    return answer

# aab bab ccc ccc ccc -> 맨 마지막에서 3ccc가 추가된다.
# aab bab ccc ccc dd -> 두 번째 else에서 2ccc가 추가되고, 맨 마지막에서는 dd만 추가된다.

if __name__ == '__main__':
    ans = solution("aabbaccc")
    print(ans)