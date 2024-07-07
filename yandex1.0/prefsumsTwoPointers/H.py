n, k = map(int, input().split())
s = input()

hash_set = dict.fromkeys(s, 0)
l = 0
freqCnt = 0
bestL, bestStart = 0, 1
for r in range(n):
    if hash_set[s[r]] == k:
        freqCnt += 1
    hash_set[s[r]] += 1
    while freqCnt > 0:
        hash_set[s[l]] -= 1
        if hash_set[s[l]] == k:
            freqCnt -= 1
        l += 1
    if r - l + 1 > bestL:
        bestL = r - l + 1
        best = l + 1
print(bestL, bestStart)

