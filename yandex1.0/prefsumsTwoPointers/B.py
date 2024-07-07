def clever_number(n: int, k: int) -> int:
    nums = list(map(int, input().split()))
    prefs = {0: 1}
    now_sum = 0
    cnt = 0
    for i in range(n):
        now_sum += nums[i]
        if now_sum - k in prefs:
            cnt += prefs[now_sum - k]
        if now_sum not in prefs:
            prefs[now_sum] = 0
        prefs[now_sum] += 1
        
    return cnt

n, k = map(int, input().split())
print(clever_number(n, k))