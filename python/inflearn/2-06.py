# 자신 숫자 전까지 2부터 나눴을 때 나눠떨어지지 않으면 소수이다.

N = int(input())
nums = list(map(int, input().split()))


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

result = ""
for num in nums:
    tmp = 0
    while num > 0:
        tmp = (tmp * 10) + num % 10
        num //= 10

    if isPrime(tmp):
        result += str(tmp) + " "

print(result)
