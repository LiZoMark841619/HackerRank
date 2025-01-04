from itertools import combinations_with_replacement

if __name__ == '__main__':
    while True:
        try:
            S, k = input('Enter a string and an integer to see its combinations with replacement! ').strip().upper().split(' ')
            string_list = list(S)
            k = int(k)
            if 0 < k <= len(S):
                combinations_ = list(combinations_with_replacement(sorted(string_list), k))
                for value in combinations_:
                    print(''.join(value))
                break
            print(f'Enter a valid k size from 1 to {len(S)}')
        except ValueError:
            print('Only integer is allowed! Try again! ')