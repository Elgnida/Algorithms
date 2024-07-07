def intersect(s1 :set[int], s2: set[int]):
    return sorted(s1 & s2)

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

print(*intersect(s1, s2))