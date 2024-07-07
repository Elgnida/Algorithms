# [1, 3, 5]
# [2, 4, 6, 8, 9]

def merge(a1: list[int], a2: list[int])->list[int]:
    c = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            c.append(a1[i])
            i += 1
        else:
            c.append(a2[j])
            j += 1

    c += a1[i:] + a2[j:]

    return c
        
def merg_sort(A):
    n = len(A)//2
    a1 = A[:n]
    a2 = A[n:]

    if len(a1) > 1:
        a1 = merg_sort(a1)
    if len(a2) > 1:
        a2 = merg_sort(a2)
    
    return merge(a1, a2)

print(merg_sort([-1, 5, 2, 0, 4, -9, 6]))