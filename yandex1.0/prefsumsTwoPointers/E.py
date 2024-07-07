n, k = map(int, input().split())

alley = list(map(int, input().split()))

hash_m = dict.fromkeys(alley, 0) # создаем словарь с уникальными цифрами
uniq_cnt = 0 # Заводим счетчик - подсчет уникальных цифр
l = 0 
bestl, bestr = 1, n
# Побежим правым указателем, левый будет догонять
for r in range(n):
    if hash_m[alley[r]] == 0: # Если до этого символ не встречался увеличиваем счетчик подсчета уникальных символов на 1
        uniq_cnt += 1
    hash_m[alley[r]] += 1 # Увеличиваем количество вхождений цифры
    while uniq_cnt == k: # Как только нашли все уникальные - начинаем двигать левый указатель
        if r - l < bestr - bestl: # Обновляем лучший отрезок
            bestl = l + 1
            bestr = r + 1
        hash_m[alley[l]] -= 1 # Удаляем цифры по левому указателю и меняем счетчик ункальных цифр
        if hash_m[alley[l]] == 0:
            uniq_cnt -= 1
        l += 1
print(bestl, bestr)