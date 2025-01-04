from collections import deque

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try: 
            value = int(input())
            if min_value < value < max_value:
                return value
        except ValueError:
            print('Invalid value! Only integer is allowed! ')

def make_actions(some_deque: deque) -> dict:
    return {
        'append':some_deque.append,
        'appendleft':some_deque.appendleft,
        'pop':some_deque.pop,
        'popleft':some_deque.popleft
    }

if __name__ == '__main__':
    N = get_valid_number(0, 101)
    d = deque()
    actions = make_actions(d)

    for _ in range(N):
        while True:
            command_input = input().split()
            command = command_input[0]
            args = map(int, command_input[1:])
            if command in actions.keys():
                actions[command](*args)
                break
    print(*d)