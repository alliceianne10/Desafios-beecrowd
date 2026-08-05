valor = int(input())

horas, resto_horas = divmod(valor,3600) 
minutos, resto_minutos = divmod(resto_horas,60)

print(f'{horas}:{minutos}:{resto_minutos}')