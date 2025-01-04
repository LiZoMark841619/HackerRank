def set_update(some_set: set, max_length) -> set:
    while True:
        some_set.update(set(map(int, input().split())))
        if 0 < len(some_set) < max_length:
            return some_set

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input())
            if value in range(min_value+1, max_value):
                return value
        except ValueError:
            print('Invalid value! Only integer is allowed! ')

A = set()
updated_A = set_update(A, max_length=501)
n = get_valid_number(0, 21)
counter = 0
for _ in range(n):
    some_set = set()
    updated_set = set_update(some_set, 101)
    if updated_A.intersection(updated_set) == updated_set:
        counter += 1
if counter == n:
    print(True)
else:
    print(False)
