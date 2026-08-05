valor = float(input())
valor = int(round(valor*100))

print ('NOTAS:')

cedulas = [10000,5000,2000,1000,500,200]
for i in cedulas:
    quant = valor//i
    print(f'{quant:.0f} nota(s) de R$ {i/100:.2f}')
    valor = valor%i

print('MOEDAS:')

moedas = [100,50,25,10,5,1]
for i in moedas:
    quant = valor//i
    print(f'{quant:.0f} moeda(s) de R$ {i/100:.2f}')
    valor = valor%i