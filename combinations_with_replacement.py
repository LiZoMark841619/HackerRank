from itertools import combinations_with_replacement

if __name__ == '__main__':
    while True:
        S, k = input().upper().split()
        try:
            k = int(k)
            if k in range(1, len(S)+1):
                comb = combinations_with_replacement(sorted(S), k)
                for value in comb:
                    print(''.join(value))
                break
            print(f'Enter a valid k size from 1 to {len(S)}')
        except ValueError:
            print('Only integer is allowed! Try again! ')