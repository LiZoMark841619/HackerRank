from itertools import combinations

if __name__ == '__main__':
    while True:
        inputs = list(input().upper().split())
        S = inputs[0]
        try:
            k = int(inputs[1])
            if k in range(1, len(S)+1):
                for counter in range(1, k+1):
                    combinations_ = combinations(sorted(S), counter)
                    for value in combinations_:
                        print(''.join(value))
                break
            print(f'Enter a valid k size from 1 to {len(S)}')
        except ValueError:
            print('Only integer is allowed! Try again! ')