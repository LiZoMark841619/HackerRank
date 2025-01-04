def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input())
            if min_value < value < max_value:
                return value
        except ValueError:
            print(f'Invalid value, try again from range {min_value}-{max_value}!')

def update_set(some_set: set, length: int) -> set:
    while len(some_set) != length:
        some_set.update(set(map(int, input().split())))
    return some_set
    
if __name__ == '__main__':
    T = get_valid_number(0, 21)
    for _ in range(T):
        length_A, A = get_valid_number(0, 1001), set()
        new_A = update_set(A, length_A)
        length_B, B = get_valid_number(0, 1001), set()
        new_B = update_set(B, length_B)
        print(True if new_A.intersection(new_B) == new_A else False)