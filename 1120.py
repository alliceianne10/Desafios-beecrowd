while True:
    falha, numero = map(str, input().split())
    if falha == '0'  and numero == '0':break

    nova_lista = []

    for num in numero:
        if num != falha:
            nova_lista.append(num)

    if len(nova_lista) == 0:
        print(0)

    else:

        valor = int(''.join(nova_lista))
        print(valor)