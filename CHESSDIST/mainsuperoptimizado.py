
for _ in range(int()):
    x1, y1, x2, y2 = map(int, input().split())
    z1 = abs(x1 - x2)
    z2 = abs(y1 - y2)
    print(max(z1, z2))
