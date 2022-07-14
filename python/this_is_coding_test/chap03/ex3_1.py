money = int(input())
count = 0

coin = [500, 100, 50, 10]

for i in coin:
    count += money // i
    money %= i

print(count)
