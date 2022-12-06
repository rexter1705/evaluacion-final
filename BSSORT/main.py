for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    a1 = a2 = a3 = a4 = n
    for i in reversed(range(n)):
        if s[i] == '1':
            zeros = []
            for j in range(a1, a2):
                if s[j] == '0':
                    zeros.append(j)
            if len(zeros) > 1:
                a3 = zeros[0]
                a4 = zeros[1]
            elif len(zeros) == 1:
                a4 = a3
                a3 = zeros[0]
            a2 = a1
            a1 = i
        ans += a4 - i
    print(ans)
