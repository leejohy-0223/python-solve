# replace 시 chaining 가능하다.
# int(숫자, 진법)을 통해 해당 진법을 10진수로 변환한다.

length = int(input())
signal = input()

result = ""
for i in range(length):
    s = signal[i * 7: i * 7 + 7]
    s = s.replace("#", "1").replace("*", "0")
    result += chr(int(s, 2))

print(result)