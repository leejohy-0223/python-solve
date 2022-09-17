import re

resultSet = set()
u_id, n_banned_id = [], []
chk = []


def dfs(L, arr):
    if L == len(n_banned_id):
        # set 확인하기
        resultSet.add(tuple(sorted(arr)))
        return

    for idx, uid in enumerate(u_id):
        if not chk[idx] and n_banned_id[L].fullmatch(uid):
            chk[idx] = True
            dfs(L + 1, arr + [uid])
            chk[idx] = False


def solution(user_id, banned_id):
    global u_id, chk
    u_id, b_id = user_id, banned_id
    chk = [False] * len(user_id)
    for b_id in banned_id:
        n_banned_id.append(re.compile(b_id.replace('*', '.')))

    dfs(0, [])

    return len(resultSet)

if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

