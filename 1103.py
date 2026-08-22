while True:
    h1, m1,h2,m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
        break
    else:
        resp = ((h2*60+m2)-(h1*60+m1))%1440 
        print(resp)