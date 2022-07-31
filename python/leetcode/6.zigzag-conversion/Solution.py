class Solution:
    def convert(self, s: str, numRows: int) -> str:

        #  numRows보다 문자열의 길이가 작다는 건 수직으로 쭉 출력하면 된다는 의미. 따라서 그냥 반환
        if numRows >= len(s):
            return s

        #  interval을 계산한다. numRows가 1이라면 interval도 1이된다.
        interval = (numRows * 2) - 2 if numRows > 1 else 1

        #  q에 탐색을 시작할 위치를 기록한다. 길이를 넘는 지점도 1회 큐에 넣는다.
        q = []
        for i in range(0, len(s) + interval, interval):
            q.append(i)

        #  제일 멀리 있는 위치보다 하나 더 크게 checker를 잡는다.
        checker = [False] * (q[-1] + 1)

        result = []
        while q:
            now = q.pop(0)

            #  위치가 s보다 작다는 건 범위 밖에 있다는 것을 의미한다. 따라서 왼쪽으로 이동만 수행
            if now > len(s):
                checker[now] = True
                q.append(now - 1)
                continue

            #  현 위치 방문 안했다면 방문을 진행한다.
            if not checker[now]:
                checker[now] = True
                result.append(now)

                #  왼쪽으로 이동하며 방문 안했으면 큐에 넣는다.
                if now - 1 >= 0 and not checker[now - 1]:
                    q.append(now - 1)

                #  오른쪽으로 이동하며 방문 안했으면 큐에 넣는다.
                if now + 1 < len(s) and not checker[now + 1]:
                    q.append(now + 1)

        #  result에 들어있는 인덱스를 s로부터 추출해서 기록한다.
        r_value = ''.join(s[i] for i in result if i < len(s))
        return r_value

if __name__ == '__main__':
    # print(Solution().convert("PAYPALISHIRING", 5))
    # print(Solution().convert("A", 1))
    # print(Solution().convert("ABCD", 3))
    print(Solution().convert("AB", 1))