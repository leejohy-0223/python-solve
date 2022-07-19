N = input()

L = int(len(N) / 2)
n1 = N[0:L]
n2 = N[L:]

sum1, sum2 = 0, 0
for i in n1:
    sum1 += int(i)

for i in n2:
    sum2 += int(i)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
