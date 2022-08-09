input1 = [input()]

lt, rt = 0, len(input1) - 1

while lt < rt:

    while not input1[lt].isalpha():
        lt += 1

    while not input1[rt].isalpha():
        rt -= 1

    if lt < rt:
        input1[lt], input1[rt] = input1[rt], input1[lt]

    lt += 1
    rt -= 1


print("".join(input1))