while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    num = input()

    lista = []
    apagados = 0
    for i in num:

        while lista and apagados < d and lista[-1] < i:
            lista.pop()
            apagados += 1
        lista.append(i)

    print(''.join(lista[0:n-d]))