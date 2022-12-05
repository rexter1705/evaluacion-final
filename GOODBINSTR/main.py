def solve(strn, s, n):
    cnt = 0
    f1 = strn.count("01")
    f2 = strn.count("10")

    for i in range(1, n - 1):
        x = f1
        y = f2
        if s[i] == '0' and s[i - 1] == '1':
            x -= 1
        if s[i] == '0' and s[i + 1] == '1':
            y -= 1
        if s[i] == '1' and s[i - 1] == '0':
            y -= 1
        if s[i] == '1' and s[i + 1] == '0':
            x -= 1
        if s[i] == '0' and s[i - 1] == '0':
            y += 1
        if s[i] == '0' and s[i + 1] == '0':
            x += 1
        if s[i] == '1' and s[i - 1] == '1':
            x += 1
        if s[i] == '1' and s[i + 1] == '1':
            y += 1
        if x == y:
            cnt += 1
    ans = False
    if abs(f1 - f2) == 1:
        ans = True
    if ans == False:
        print(cnt)
    else:
        print(cnt+2)


for _ in range(int(input())):
    strn = input().strip()
    s = list(strn)
    n = len(s)
    solve(strn, s, n)
