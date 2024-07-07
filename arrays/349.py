nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 5, 1, 5, 2, 3]
seen = set(nums1)
res = []
for i in nums2:
    if i in seen:
        res.append(i)
        seen.remove(i)
print(res)