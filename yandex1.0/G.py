n, k, m = map(int, input().split())

free = n // k
valid = n - free * k

s = free * (k // m)
s_weight = s * m
if free * k - s_weight + valid >= k:
    free = (free * k - s_weight + valid) // k
    s += free * (k // m)
print(s)
