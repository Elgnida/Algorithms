# 1 3 5 7 9 
# 2 4 8 1 6 


n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in list2:
    l = 0
    r = len(list1) - 1
    while l < r:
        mid = (r + l) // 2
        if list1[mid] < i:
            l = mid + 1
        else:
            r = mid
    if l > 0 and list1[l] != i and abs(list1[l - 1] - i) <= abs(list1[l] - i):
        print(list1[l-1])
    else:
        print(list1[l])
