s = float(input())

if 0 <= s <= 2000:
    print('Isento')

elif s <= 3000:
    imposto = (s - 2000) * 0.08
    print(f'R$ {imposto:.2f}')

elif s <= 4500:
    imposto = (s - 3000) * 0.18 + 80
    print(f'R$ {imposto:.2f}')

else:
    imposto = (s - 4500) * 0.28 + 350
    print(f'R$ {imposto:.2f}')