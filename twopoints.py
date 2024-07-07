#[1, 3, 5, 7, 8], target = 4, O(n) time space, O(1) - memory space

def cntpairs(nums: list[int], target: int) -> int:
    cntpairs = 0
    right = 0
    for left in range(len(nums)):
        while right < len(nums) and nums[right] - nums[left] <= target:
            right += 1
        cntpairs += len(nums) - right
    return cntpairs

print(cntpairs([1, 3, 5, 7, 8], 2))