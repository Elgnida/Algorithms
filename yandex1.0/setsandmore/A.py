def unique(nums: list[int]):
    uniq = set()

    for i in nums:
        if i not in uniq:
            uniq.add(i)
    return len(uniq)
n = list(map(int, input().split()))
print(unique(n))