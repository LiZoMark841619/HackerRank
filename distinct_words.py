from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

word_counting = Counter(words)
result = set(words)

print(len(result))
print(*list(word_counting.values()), sep=' ')