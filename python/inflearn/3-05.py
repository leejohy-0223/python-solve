n = int(input())

lt, rt = 1, 2
numSum = 3
result = 0
while lt != rt:
    # sum이 크거나 같을 경우에는 lt 옮기기
    if numSum >= n:
        result += 1 if numSum == n else 0
        numSum -= lt
        lt += 1
    else:
        rt += 1
        numSum += rt
print(result)