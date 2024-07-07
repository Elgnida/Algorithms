def synonym(n: int):
    synonyms = {}
    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1
    word3 = input()
    return synonyms[word3]

n = int(input())
print(synonym(n))
