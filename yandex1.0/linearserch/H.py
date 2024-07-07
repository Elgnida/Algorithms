def find_three(nums: list[int]) -> list[int]:
    num3 = nums[:3]
    max1 = max(num3)
    num3.remove(max1)
    max3 = min(num3)
    num3.remove(max3)
    max2 = num3[0]
    for i in range(3, len(nums)):
        if nums[i] > max1:
            max3 = max2
            max2 = max1
            max1 = nums[i]
        elif nums[i] > max2:
            max3 = max2
            max2 = nums[i]
        elif nums[i] > max3:
            max3 = nums[i]

    num3 = nums[:3]
    min3 = max(num3)
    num3.remove(min3)
    min1 = min(num3)
    num3.remove(min1)
    min2 = num3[0]
    for i in range(3, len(nums)):
        if nums[i] < min1:
            min3 = min2
            min2 = min1
            min1 = nums[i]
        elif nums[i] < min2:
            min3 = min2
            min2 = nums[i]
        elif nums[i] < min3:
            min3 = nums[i]

    p1 = min1*min2*max1
    p2 = max1*max2*max3
    if p1 > p2:
        return min1, min2, max1
    else:
        return max1, max2, max3
            
    
n = list(map(int, input().split()))
print(*find_three(n))