from itertools import combinations

if __name__ == '__main__':
    while True:
        try:
            S, k = input('Enter a string and an integer to see its combinations until that number! ').strip().upper().split(' ')
            string_list = list(S)
            k = int(k)
            if 0 < k <= len(S):
                counter = 1
                while counter <= k:
                    combinations_ = list(combinations(sorted(string_list), counter))
                    for value in combinations_:
                        print(''.join(value))
                    counter += 1
                break
            print(f'Enter a valid k size from 1 to {len(S)}')
        except ValueError:
            print('Only integer is allowed! Try again! ')