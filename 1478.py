while True:
    N = int(input())

    if N == 0:
        break
    
    matriz = []
    for i in range(N):
        linhas = []
        for j in range(N):
            valor = abs(i-j) + 1
            linhas.append(valor)
        matriz.append(linhas)
    
    for i in range(N):
        linha_formatada = ''
        for j in range(N):
            linha_formatada += f'{matriz[i][j]:3d}'

            if j< N-1:
                linha_formatada +=' '
        print(linha_formatada)
    print()
