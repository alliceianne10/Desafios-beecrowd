a,b = map(float, input().split())

dif = abs(a-b)
por = 100 * dif/a

print(f'{por:.2f}%')