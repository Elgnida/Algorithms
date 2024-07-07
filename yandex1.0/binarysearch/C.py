w, h, n = map(int, input().split())

l = 0
r = max(w, h) * n

def check(m, w, h):
    return (m // w) * (m // h) >= n

def rbinserch(l, r, check):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, w, h):
            r = m - 1
        else:
            l = m
    return l + 1

print(rbinserch(l, r, check))