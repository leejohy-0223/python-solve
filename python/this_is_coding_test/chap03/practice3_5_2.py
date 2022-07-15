a, b = map(int, input().split())
ball = list(map(int, input().split()))

array = [0] * 11

for i in ball:
    array[i] += 1

# 1 : 1개
# 2 : 2개
# 3 : 2개

# A가 1을 고르면 B는 선택지 a - arr[1]개 (첫 배열 빼야함)
result = 0
for i in array:
    if i != 0:
        a -= i
        result += (i * a)

print(result)
