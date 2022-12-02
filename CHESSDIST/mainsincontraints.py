


print('Ingrese el número de casos T')
T = int(input())

for _ in range(int(T)):

    print('Ingrese los valores de las parejas en el plano cartesiano.')
    x1, y1, x2, y2 = map(int, input().split())
    z1 = abs(x1 - x2)
    z2 = abs(y1 - y2)
    print(max(z1, z2))
