N = int(input())

for i in range(N):
    a = str(input())

    cont = 0 
    for num in a:
        match num:
            case '1':
                cont += 2
            case '2' | '3' | '5':
                 cont += 5
            case '4':
                cont += 4
            case '6' | '9' |'0':
                cont += 6
            case '7':
                cont += 3
            case '8':
                cont += 7

    print(f'{cont} leds')
            