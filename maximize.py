from itertools import product

while True:
    inputs = input().split()
    try:
        values = list(map(int, inputs))
        if len(values) != 2:
            continue
        K, M = values
        if K in range(1, 8) and M in range(1, 1001):
            break
    except ValueError:
        print('Only integer is allowed! Try again! ')

result = []
for _ in range(K):
    while True:
        inputs = input().split()
        try:
            values = map(int, inputs)
            N, *rest = values
            if N not in range(1, 8):
                continue
            if all(value in range(1, 10**9+1) for value in rest):
                result.append(rest)
                break
        except ValueError:
            print('Only integer is allowed! ')
            
print(max(sum(map(lambda x: x**2, combo))%M for combo in product(*result)))
