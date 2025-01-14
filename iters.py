from string import ascii_lowercase
from itertools import combinations

while True:
    N = int(input())
    if N in range(1, 11):
        break

string_list: list[str] = []
while len(string_list) != N:
    for value in input().split():
        if value not in ascii_lowercase:
            continue
        string_list.append(value)
        
while True:
    K = int(input())
    if K in range(1, N+1):
        break

total_combinations = 0
target_combinations = 0

for comb in combinations(string_list, K):
    total_combinations += 1
    if 'a' in comb:
        target_combinations +=1
        
final = target_combinations / total_combinations
print(f'{final}')
#print(result)