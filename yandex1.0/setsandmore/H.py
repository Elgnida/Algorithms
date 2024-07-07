n = int(input())
s = set()

for i in range(n):
    x = int(input().split()[0])
    s.add(x)

print(len(s))


