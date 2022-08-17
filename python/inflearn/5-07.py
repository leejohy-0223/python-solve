from collections import deque

def solution():
    necessary = input()
    schedule = input()

    q = deque([i for i in necessary])

    for s in schedule:
        if s in q:
            if q[0] != s:
                return "NO"
            else:
                q.popleft()

    return "YES" if len(q) == 0 else "NO"

if __name__ == '__main__':
    print(solution())