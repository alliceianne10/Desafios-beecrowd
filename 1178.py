X = float(input())
lista = [X]

for i in range(99):
    X = X/2
    lista.append(X)

for i in range(100):
    print(f'N[{i}] = {lista[i]:.4f}')