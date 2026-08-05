d1 = int(input().split()[1])
h1, m1, s1 = (map(int, input().split(':')))

#Tempo final:
d2 = int(input().split()[1])
h2, m2, s2 = (map(int,input().split(':')))


tempo_evento_s = ((d2*86400)+(h2*3600)+(m2*60)+(s2))-((d1*86400)+(h1*3600)+(m1*60)+(s1)) 
dias = tempo_evento_s//86400
horas = (tempo_evento_s%86400)//3600
minutos = ((tempo_evento_s%86400)%3600)//60
segundos = ((tempo_evento_s%86400)%3600)%60

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')