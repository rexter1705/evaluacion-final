
for _ in range(int(input())):
    n, w = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        if w % i == 0:
            a = w // i
            if a <= n and a <= (abs(i - n) + 1):
                cnt += 1
    if cnt == 0:
        print("NO")
    else:
        print("Si")
