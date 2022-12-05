def solve(strg, s, n):
    cnt = 0
    x = s1.count("01")
    y = s1.count("10")

    for i in range(1, n - 1):
        a = x
        b = x
        if (s[i] == '0' and s[i - 1] == '1'):
            a -= 1
        if (s[i] == '0' and s[i + 1] == '1'):
            b -= 1
        if (s[i] == '1' and s[i - 1] == '0'):
            b -= 1
        if (s[i] == '1' and s[i + 1] == '0'):
            a -= 1
        if (s[i] == '0' and s[i - 1] == '0'):
            b += 1
        if (s[i] == '0' and s[i + 1] == '0'):
            a += 1
        if (s[i] == '1' and s[i - 1] == '1'):
            a += 1
        if (s[i] == '1' and s[i + 1] == '1'):
            b += 1
        if (a == b):
            cnt += 1
    ans = False
    if abs(f1 - f2) == 1:
        ans = True
    if ans == False:
        print(cnt)
        return
    if (s[0] == s[1]):
        if (s[0] == '0') or (s[0] == '1'):
            cnt += 1
    else:
        if (s[0] == '0') or (s[0] == '1'):
            cnt += 1
    if (s[n - 1] == s[n - 2]):
        if (s[n - 1] == '0') or (s[n - 1] == '1'):
            cnt += 1
    else:
        if (s[n - 1] == '0') or (s[n - 1] == '1'):
            cnt += 1
    print(cnt)


for _ in range(int(input())):
    strg = input().strip()
    s = list(strg)
    n = len(s)
    solve(strg, s, n)
