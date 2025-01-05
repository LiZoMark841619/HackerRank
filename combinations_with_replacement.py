from itertools import combinations_with_replacement

if __name__ == '__main__':
    while True:
        inputs = list(input().upper().split())
        S = list(inputs[0])
        try:
            k = int(inputs[1])
            if k in range(1, len(S)+1):
                combinations_ = combinations_with_replacement(sorted(list(S)), k)
                for value in combinations_:
                    print(''.join(value))
                break
            print(f'Enter a valid k size from 1 to {len(S)}')
        except ValueError:
            print('Only integer is allowed! Try again! ')