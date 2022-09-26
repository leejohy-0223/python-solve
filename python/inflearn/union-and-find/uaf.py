unf = []


def find(v):
    if unf[v] == v:
        return v
    unf[v] = find(unf[v])
    return unf[v]


def union(frd1, frd2):
    frd1 = find(frd1)
    frd2 = find(frd2)

    if frd1 != frd2:
        unf[frd1] = frd2


def solution(friends, ch1, ch2):
    for frd1, frd2 in friends:
        union(frd1, frd2)

    return find(ch1) == find(ch2)


if __name__ == '__main__':
    n1, m1 = map(int, input().split())
    friend = []
    unf = [i for i in range(0, n1 + 1)]
    for _ in range(m1):
        f1, f2 = map(int, input().split())
        friend.append((f1, f2))

    c1, c2 = map(int, input().split())

    print(solution(friend, c1, c2))