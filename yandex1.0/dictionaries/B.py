def counting(words: list[str]):
    counts = []
    dict_count = {}

    for word in words:
        if word not in dict_count:
            dict_count[word] = 0
            counts.append(dict_count[word])
        else:
            dict_count[word] += 1
            counts.append(dict_count[word])
    return counts

n = open('yandex1.0\dictionaries\input.txt', 'r')
words = n.read().split()

print(*counting(words))