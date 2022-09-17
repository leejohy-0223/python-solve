from itertools import permutations
import re

def solution(user_id, banned_id):
    n_banned_id = []
    for b_id in banned_id:
        n_banned_id.append(re.compile(b_id.replace('*', '.')))

    perm_list = permutations(user_id, len(banned_id))
    resultSet = set()
    for perm in perm_list:
        for idx, b_id in enumerate(n_banned_id):
            if not b_id.fullmatch(perm[idx]):
                break
        else:
            resultSet.add(tuple(sorted(list(perm))))

    return len(resultSet)

if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

