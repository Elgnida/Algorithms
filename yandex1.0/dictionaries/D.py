def keyboard(n_keys: int):
    hs_mp = {}
    strength = list(map(int, input().split()))
    for i in range(1, n_keys + 1):
        hs_mp[i] = strength[i-1]
    total = int(input())
    press = list(map(int, input().split()))
    for i in range(total):
        hs_mp[press[i]] -= 1
    for val in hs_mp.values():
        if val < 0:
            print('YES')
        else:
            print('NO')

n_keys = int(input())
keyboard(n_keys)