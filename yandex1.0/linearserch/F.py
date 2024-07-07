def symmetric(n: int, nums: list[int]):
    left = 0
    right = n - 1
    add = 0

    while left < right:
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        else:
            right = n - 1
            left += 1
            add = left
    return str(add), ' '.join(str(i) for i in nums[:add][::-1])





n = int(input())
nums = list(map(int, input().split()))
a, b = symmetric(n, nums)
print(a + '\n' + b)