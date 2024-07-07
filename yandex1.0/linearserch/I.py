def makefield(n, m, mines):
    dx = (-1, -1, -1, 0, 1, 1, 1, 0)
    dy = (-1, 0, 1, 1, 1, 0, -1, -1)

    field = []

    for k in range(n + 2):
        field.append([0] * (m + 2))

    for minei, minej in mines:
        for i in range(len(dx)):
            field[minei + dx[i]][minej + dy[i]] += 1
    for minei, minej in mines:
        field[minei][minej] = '*'

    for i in range(len(field)):
        field[i] = field[i][1:-1]
    
    return field[1: -1]


n, m, k = list(map(int, input().split()))
mines = []
for i in range(k):
    mines.append(tuple(map(int, input().split())))
ans = makefield(n, m, mines)
for i in range(len(ans)):
    print(*ans[i])