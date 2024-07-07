# 50 60 74 82 100 120 

n, d = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
boats = 0
r = len(weights) - 1
for l in range(len(weights)):
    while r > l and weights[l] + weights[r] > d:
        r -= 1
        boats += 1
    if l > r:
        break
    else:
        r -= 1
        boats += 1

print(boats)
        