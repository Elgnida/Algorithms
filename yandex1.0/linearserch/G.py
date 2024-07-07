def find_two(nums: list[int]):
    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])

    min1 = max(nums[0], nums[1])
    min2 = min(nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i] > max2:
            max2 = nums[i]

    for i in range(2, len(nums)):
        if nums[i] < min2:
            min1 = min2
            min2 = nums[i]
        elif nums[i] < min1:
            min1 = nums[i]

    if min1 * min2 > max1 * max2:
        if min1 > min2:
            return min2, min1
        else:
            return min1, min2
    else:
        if max2 > max1:
            return max1, max2
        else:
            return max2, max1
nums = find_two(list(map(int, input().split())))
print(nums[0], nums[1])