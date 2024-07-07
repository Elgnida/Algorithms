# 10 10
# 1 61 126 217 2876 6127 39162 98126 712687 1000000000 
# 100 6127 1 61 200 -10000 1 217 10000 1000000000 



n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for val in list2:
    l = 0
    r = len(list1) - 1
    while l <= r:
        mid = (l + r) // 2
        if list1[mid] > val:
            r = mid - 1
        elif list1[mid] < val:
            l = mid + 1
        elif list1[mid] == val:
            print('YES')
            break
    else:
        print("NO")