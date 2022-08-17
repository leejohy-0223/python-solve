from collections import deque

def solution():
    N, K = map(int, input().split())
    q = deque([i for i in range(1, N + 1)])

    cnt = 1
    while len(q) != 1:
        now = q.popleft()
        if cnt == K:
            cnt = 1
            continue
        else:
            q.append(now)
            cnt += 1

    return q[0]

if __name__ == '__main__':
    print(solution())
