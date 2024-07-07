# def gen(g1, g2):
#     i = 0
#     j = 1
#     set1 = {}
#     count = 0
#     while j != len(g2):
#         if g2[i:j+1] not in set1:
#             set1[g2[i:j+1]] = 1
#             j += 1
#             i += 1
#         else:
#             set1[g2[i:j+1]] += 1
#             j += 1
#             i += 1

    
#     i = 0
#     j = 1
#     while j != len(g1):
#         count += set1.get(g1[i:j+1], 0)
#         i += 1
#         j += 1

#     return count
# genom1 = input()
# genom2 = input()

# print(gen(genom1, genom2))
s1 = input()
s2 = input()
pairs = set()
for i in range(len(s2) - 1):
    pairs.add(s2[i:i + 2])
ans = 0
for i in range(len(s1) - 1):
    if s1[i: i + 2] in pairs:
        ans += 1
print(ans)
