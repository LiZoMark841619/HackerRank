from collections import deque

def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        try: 
            value = int(input())
            if min_value < value < max_value:
                return value
            else:
                print('Invalid range! Try again! ')
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
            try:
                args = map(int, command_input[1:])
            except ValueError:
                print('Only integer is allowed! Try again! ')
            if command in actions.keys():
                try:
                    actions[command](*args)
                    break
                except TypeError:
                    print('Invalid argument! Try again! ')
            print('Invalid command! Try again!')
    print(*d)