from collections import deque

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input())
            if value in range(min_value, max_value+1):
                return value
        except ValueError:
            print('Invalid value! Try again with iteger! ')

def deque_updating(some_deque: deque, max_length: int) -> deque:
    while len(some_deque) != max_length:
        some_deque.extend(map(int, input().split()))
    return some_deque

def pop_left_right(some_deque: deque, empty: deque) -> deque:
    while some_deque:
        empty.append(some_deque.pop() if some_deque[0] <= some_deque[-1] else some_deque.popleft())
    return empty
    
if __name__ == '__main__':
    T = get_valid_number(1, 5)
    for _ in range(T):
        some_deque:deque[int] = deque()
        empty:deque[int] = deque()
        n = get_valid_number(1, 10**5)
        updated_deque = deque_updating(some_deque, n)
        max_value, min_value = max(updated_deque), min(updated_deque)
        result = pop_left_right(updated_deque, empty)
        print('Yes' if result[0] == max_value and result[-1] == min_value else 'No')