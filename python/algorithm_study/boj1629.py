import sys
input = sys.stdin.readline


def manual_pow(x, y, z):
    if y == 1:
        return x % z

    temp = manual_pow(x, y // 2, z)

    if temp % 2 == 0:
        return temp * temp % z
    else:
        return temp * temp * x % z


if __name__ == '__main__':
    a, b, c = map(int, input().split())

    print(manual_pow(a, b, c))