def calc(n, m, k, number):
    unique = set([n, m, k])
    count = 0
    for i in number:
        if int(i) not in unique:
            unique.add(int(i))
            count += 1
    return count


n, m, k = map(int, input().split())
number = list(input())
print(calc(n, m, k, number))
