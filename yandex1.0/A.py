tr, tc = map(int, input().split())
mode = input()

if mode == 'heat':
    if tr < tc:
        print(tc)
    else:
        print(tr)
elif mode == 'freeze':
    if tr < tc:
        print(tr)
    else:
        print(tc)
elif mode == 'fan':
    print(tr)
elif mode == 'auto':
    if tr > tc:
        print(tc)
    elif tr < tc:
        print(tc)
    else:
        print(tr)

