a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0 and c == 0:
        print('MANY SOLUTIONS')
    elif c**2 == b:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
    
elif c < 0:
    print('NO SOLUTION')

elif a != 0:
    if (c**2 - b) % a == 0:
        print((c**2 - b) // a)
    else:
        print('NO SOLUTION')

