# numbers = [2,7,11,15], target = 9

# def twoSum(numbers: list[int], target: int) -> list[int]:
#     hash_m = {} # O(n) память
#     for l in range(len(numbers)):
#         if target - numbers[l] in hash_m:
#             return hash_m[target - numbers[l]] + 1, l + 1
#         hash_m[numbers[l]] = l

# print(twoSum(numbers = [2,7,11,15], target = 9))

def twoSum(numbers: list[int], target: int) -> list[int]:
    r = len(numbers) - 1
    for l in range(len(numbers)):
        while l < r and numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] == target:
            return l + 1, r + 1

print(twoSum(numbers = [2,7,11,15], target = 9))