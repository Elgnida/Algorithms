def common_word(words: list[str]):
    freq = {}

    for word in words:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    max_count = 0
    word = ''
    for key in freq.keys():
        if freq[key] > max_count:
            max_count = freq[key]
            word = key
        elif max_count == freq[key]:
            word = min(word, key)
    return word
n = open('yandex1.0\dictionaries\input.txt', 'r')

words = n.read().split()
print(common_word(words))
