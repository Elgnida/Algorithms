# def pref_sum(n: list[int]):
#     prefs = [0] * (len(n) + 1)

#     for i in range(1, len(n) + 1):
#         prefs[i] = prefs[i-1] + n[i - 1]

#     return prefs

# def rsq(prefs, l, r):
#     return prefs[r] - prefs[l]

# print(rsq(pref_sum([1, 2, 3]), 0, 3))

def makePrefZeros(nums: list[int]) -> int:
    pref_zeros = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            pref_zeros[i] = pref_zeros[i - 1] + 1
        else:
            pref_zeros[i] = pref_zeros[i - 1]
    return pref_zeros

def countZeros(pref, l ,r):
    return pref[r] - pref[l]

print(countZeros(makePrefZeros([1, 0, 0, 3, 4, 0, 0, 1]), 0, 7))