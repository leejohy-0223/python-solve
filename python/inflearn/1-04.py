n = int(input())

for i in range(n):
    now = list(input())

    lt, rt = 0, len(now) - 1
    while lt < rt:
        now[lt], now[rt] = now[rt], now[lt]
        lt += 1
        rt -= 1

    print(''.join(now))

