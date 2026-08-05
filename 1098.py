for i in range(0, 21, 2):
    i = i / 10
    
    for k in range(1, 4):
        j = i + k
        
        if i % 1 == 0:
            print(f"I={i:.0f} J={j:.0f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")