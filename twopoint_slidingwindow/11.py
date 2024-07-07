def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    maxArea = 0
    while r > l:
        width = r - l
        minhigh = min(height[r], height[l])
        maxArea = max(maxArea, width * minhigh)
        if minhigh == height[r]:
            r -= 1
        else:
            l += 1
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))