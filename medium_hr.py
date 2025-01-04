import random
from collections import Counter 

K, M = map(int, input().split())
D = {}
for _ in range(K):
    data = list(map(int, input().split()))
    length_of_array = data[0]
    array = data[1:]
    D[length_of_array] = [value ** 2 for value in array]


counter = 1
for k in D:
    counter *= k

final = []
while len(final) != counter:
    result = []
    for k in D:
        random_picking = random.choice(D[k])
        result.append(random_picking)
    if result not in final:
        final.append(result)
        
final.sort()
result = []
for value in final:
    result.append(sum(value)%1000)
result.sort()
print(result[-1])


    
    
    
    