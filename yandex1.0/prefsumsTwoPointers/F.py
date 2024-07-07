n = int(input())
classes = sorted(list(map(int, input().split())))
m = int(input())
cond = {}
out = 0
for _ in range(m):
    i, j = map(int, input().split())
    if i not in cond or cond[i] > j:
        cond[i] = j
cond = sorted(cond.items(), key=lambda x: x[1])
r = 0
for l in classes:
    while r < len(cond):
        if l <= cond[r][0]:
            out += cond[r][1]
            break
        else:
            r += 1
print(out)