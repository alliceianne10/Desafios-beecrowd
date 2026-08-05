while True:
    try:
        lista = []

        dias = int(input())
        custo_dia = int(input())

        for i in range(dias):
            lista.append(int(input()))

        maior_lucro = 0
        for i in range(1,dias+1):
            comb = dias - i + 1 
            for j in range(comb):
                lucro = sum (lista[j:j+i]) - (custo_dia * i)

                if lucro > maior_lucro:
                    maior_lucro = lucro 

        print(maior_lucro)

    except EOFError:
        break