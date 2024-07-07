n, a, b, w, h = map(int, input().split())

l = 0
r = max(w, h)

def check(m, w, h):
    return (w // (b + 2*m)) * (h // (a + 2*m)) < n and (w // (a + 2*m)) * (h // (b + 2*m)) < n

def rbinsearch(l, r, check):
    while l + 1 < r:
        m = (l + r) // 2
        if check(m, w, h):
            r = m
        else:
            l = m
    return l

print(rbinsearch(l, r, check))

