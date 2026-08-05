valor = int(input())
print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    quant = valor//cedula
    print(f'{quant} nota(s) de R$ {cedula},00')
    valor -= quant*cedula