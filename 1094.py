N = int(input())
coe = rat = sap = 0
for i in range(N):
    num, cob = map(str, input().split())
    num = int(num)
    if cob == 'C':
        coe += num
    elif cob == 'R':
        rat += num
    else:
        sap += num
total = sap + coe + rat
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coe}')
print(f'Total de ratos: {rat}')
print(f'Total de sapos: {sap}')
print(f'Percentual de coelhos: {(coe/total)*100:.2f} %')
print(f'Percentual de ratos: {(rat/total)*100:.2f} %')
print(f'Percentual de sapos: {(sap/total)*100:.2f} %')