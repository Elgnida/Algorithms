a, b, c = int(input()), int(input()), int(input())
s = a + b + c
ss = 2*a + 3*b + 4*c
l = 0
r = 4 * s + 1
while l + 1 < r:
    m = (l + r) // 2
    if (ss + m*5)*2 >= 7 * (s + m):
        r = m
    else:
        l = m
print(r)
