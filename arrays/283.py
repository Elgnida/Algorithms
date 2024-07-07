def zeros(nums):

    zero_ind = None

    for i in range(len(nums)):
        if (nums[i] == 0) and (zero_ind is None):
            zero_ind = i
            continue
        if (zero_ind is not None) and (nums[i] != 0):
            nums[zero_ind], nums[i] = nums[i], nums[zero_ind]
            zero_ind += 1
    print(nums)
zeros([5, 1, 0, 3, 4, 1, 123, 0, 0, 8, 9, 0, 10])