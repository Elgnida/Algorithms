# 4 5
# 3 1 2 1



n, t = map(int, input().split())
books = list(map(int, input().split()))
maxLen = 0 
curSum = 0
l = 0
for r in range(n):
    curSum += books[r]

    while curSum > t:
        curSum -= books[l]
        l += 1
    maxLen = max(maxLen, r - l + 1)
print(maxLen)