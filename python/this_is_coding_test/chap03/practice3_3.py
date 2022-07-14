s = input()


def calculate_count(a, b):
    count = 0
    chk = True
    for i in s:
        if chk and i == a:
            chk = False
            count += 1
        elif i == b and not chk:
            chk = True
    return count


print(min(calculate_count('0', '1'), calculate_count('1', '0')))
