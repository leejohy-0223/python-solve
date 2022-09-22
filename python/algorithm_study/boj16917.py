def solution(spicyPrice, friedPrice, hAndhPrice, minSpicy, minFried):
    minPrice = 10e8
    spicyCount, friedCount = minSpicy, minFried
    count = max(spicyCount, friedCount)

    hAndhCount = 0
    for _ in range(count + 1):
        price = (spicyCount * spicyPrice) + (friedCount * friedPrice) + (hAndhCount * hAndhPrice)
        minPrice = min(minPrice, price)
        spicyCount = spicyCount - 1 if spicyCount >= 1 else 0
        friedCount = friedCount - 1 if friedCount >= 1 else 0
        hAndhCount += 2

    return minPrice


if __name__ == '__main__':
    a, b, c, x, y = map(int, input().split())
    print(solution(a, b, c, x, y))