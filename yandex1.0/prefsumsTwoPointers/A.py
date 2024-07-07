def style(s: int, shirts: list[int], t: int, shorts: list[int]) -> list[int]:
    right = 0
    min_sub = None
    pairs = [0, 0]
    for left in range(s):
        while right < t:
            if min_sub == None or (abs(shirts[left] - shorts[right]) < min_sub):
                min_sub = abs(shirts[left] - shorts[right])
                pairs[0] = shirts[left]
                pairs[1] = shorts[right]
            if shirts[left] < shorts[right]:
                break
            else:
                right += 1
 

    return pairs

s = int(input())
shirts = list(map(int, input().split()))
t = int(input())
shorts = list(map(int, input().split()))

print(*style(s, shirts, t, shorts))