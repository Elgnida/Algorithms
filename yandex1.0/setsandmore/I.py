def polygloti(n: int):
    
    count = 0
    for _ in range(n):
        l = int(input())
        for _ in range(l):
            langueg = input()
            if langueg not in langueges:
                langueges[langueg] = 0
            langueges[langueg] += 1
    for key in langueges.keys():
        if langueges[key] == n:
            count += 1
            all_knows.add(key)
    return count, len(langueges)
langueges = {}
all_knows = set()
n = int(input())
asks = polygloti(n)
print(asks[0])
for i in range(asks[0]):
    print(all_knows.pop())
print(asks[1])
for i in langueges.keys():
    print(i)