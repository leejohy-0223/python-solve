input_data = input()
row = int(input_data[1])
column = ord(input_data[0])

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

count = 0
for step in steps:
    nRow = row + step[0]
    nColumn = column + step[1]

    if nRow < 1 or nRow > 8 or nColumn < ord('a') or nColumn > ord('h'):
        continue
    count += 1
    print(nRow, nColumn)

print(count)