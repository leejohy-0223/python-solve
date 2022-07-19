N = int(input())

ix, iy = 1, 1

arr = list(input().split())

for i in arr:
    if i == 'L':
        if iy > 1:
            iy -= 1
    elif i == 'R':
        if iy < N:
            iy += 1
    elif i == 'U':
        if ix > 1:
            ix -= 1
    else:
        if ix < N:
            ix += 1

print(ix, iy)

