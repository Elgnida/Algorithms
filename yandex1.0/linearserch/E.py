def lepehska(n: int, nums: list[int]) -> int:
    champ = 0
    for i in range(len(nums)):
        if nums[i] > nums[champ]:
            champ = i
    vasiliy = 1
    temp = None
    for j in range(champ + 1, len(nums) - 1):
        if nums[j] % 10 == 5 and nums[j] > nums[j + 1]:
            if temp == None:
                temp = j
            elif nums[j] > nums[temp]:
                temp = j
    if temp == None:
        return 0
    for k in range(len(nums)):
        if nums[k] > nums[temp]:
            vasiliy += 1
        
    return vasiliy




n, nums = int(input()), list(map(int, input().split()))
print(lepehska(n, nums))

