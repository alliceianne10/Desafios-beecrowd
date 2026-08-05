numero = int(input())
a = 0
b = 1
lista = []

for i in range (numero):
    lista.append(str(a))
    a, b = b, a + b

print(' '.join(lista))