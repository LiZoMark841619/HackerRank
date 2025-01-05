from string import ascii_lowercase
from itertools import combinations

N = 0
while N not in range(1, 11):
    N += int(input())

string_list = []
while len(string_list) != N:
    for value in input().split():
        if value not in ascii_lowercase:
            continue
        string_list.append(value)

K = 0
while K not in range(1, N+1):
    K += int(input())

idxs = range(1, len(string_list) + 1)
result = list(combinations(idxs, K))
counter = 0
for value in result:
    for val in value:
        if string_list[val-1] == 'a':
            counter += 1
            break

final = counter / len(result)
print(f'{final}')