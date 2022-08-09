s = input()
lt, rt = 0, len(s) - 1

while lt < rt:
    if s[lt].lower() != s[rt].lower():
        print("NO")
        break
    lt += 1
    rt -= 1

else:
    print("YES")
