def cntMonument(n, r):
    right = 0
    monuments = list(map(int, input().split()))
    cnt = 0
    for left in range(n):
        while right < n and  monuments[right] - monuments[left] <= r:
                right += 1
        cnt += n - len(monuments[:right])
    return cnt


n, r = map(int, input().split())
print(cntMonument(n, r))