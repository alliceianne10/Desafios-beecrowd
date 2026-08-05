O = input()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = sum (matriz[0][1:11]) + sum(matriz[1][2:10]) + sum(matriz[2][3:9]) + sum(matriz[3][4:8]) + sum(matriz[4][5:7])

if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/30:.1f}')