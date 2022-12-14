T = 0

while True: #Se ingresan los ciclos While debido a que en los puntos extra debiamos añadir constraints
    try:
        print('Ingrese el número de casos T')
        T = int(input())
    except ValueError:
        print('Por favor ingrese un número de casos valido')
        continue
    if 1 <= T <= 1000:
        break
    else:
        print('Por favor un número de casos dentro del rango 1 a 1000')

for _ in range(int(T)):
    x1 = 0
    while True:
        try:
            print('Ingrese los valores de las parejas en el plano cartesiano.')
            x1, y1, x2, y2 = map(int, input().split())
        except ValueError:
            print('Por favor ingrese coordenadas validas')
            continue
        if 1 <= x1 <= 100000 and 1 <= y1 <= 100000 and 1 <= x2 <= 100000 and 1 <= y2 <= 100000:
            break
        else:
            print('Por favor coordenadas en el rango de 1 a 100000')

    z1 = abs(x1 - x2)
    z2 = abs(y1 - y2)
    print(max(z1, z2))
