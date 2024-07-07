nums = list(map(int, input().split()))

def mono(nums: list[str]):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return 'NO'
    return 'YES'

print(mono(nums))