n = int(input())
english = set()
while len(english) != n:
    english.update(set(map(int, input().split())))
    break
b = int(input())
french = set()
while len(french) != b:
    french.update(set(map(int, input().split())))
    break
print(len(english.union(french)))

n = int(input())
english = set()
while len(english) != n:
    english.update(set(map(int, input().split())))
    break
b = int(input())
french = set()
while len(french) != b:
    french.update(set(map(int, input().split())))
    break
print(len(english.intersection(french)))

n = int(input())
english = set()
while len(english) != n:
    english.update(set(map(int, input().split())))
    break
b = int(input())
french = set()
while len(french) != b:
    french.update(set(map(int, input().split())))
    break
print(len(english.difference(french)))

n = int(input())
english = set()
while len(english) != n:
    english.update(set(map(int, input().split())))
    break
b = int(input())
french = set()
while len(french) != b:
    french.update(set(map(int, input().split())))
    break
print(len(english.symmetric_difference(french)))