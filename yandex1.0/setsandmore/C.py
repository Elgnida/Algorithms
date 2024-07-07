def cube(n: int, m: int):
    n_set = set()
    m_set = set()

    for i in range(n):
        k = int(input())
        n_set.add(k)
    for j in range(m):
        l = int(input())
        m_set.add(l)

    set1 = n_set.intersection(m_set)
    count1 = len(set1)
    set2 = n_set - m_set
    count2 = len(set2)
    set3 = m_set - n_set
    count3 = len(set3)

    return count1, sorted(set1), count2, sorted(set2), count3, sorted(set3)

n, m = map(int, input().split())
ask = cube(n, m)

for i in ask:
    if type(i) == list:
        print(*i)
    else:
        print(i)

    