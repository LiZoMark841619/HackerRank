def take_actions(L: list) -> dict:
    return {'print': lambda: print(L),
            'remove': L.remove,
            'append': L.append,
            'sort': L.sort,
            'pop': L.pop,
            'reverse': L.reverse,
            'insert': L.insert}

if __name__ == '__main__':
    while True:
        min_val, max_val = 1, 10
        N = int(input(f'Set a value from {min_val} to {max_val}! '))
        if N in range(min_val, max_val+1):
            print(f'Well done! Your chosen value is {N}. ')
            break
        else:
            print('Out of range! Try again!')
    
    L: list[int] = []
    actions = take_actions(L)

    for _ in range(N):
        while True:
            command_input = input().split()
            command = command_input[0]
            if command in actions.keys():
                try:
                    args = map(int, command_input[1:])
                    actions[command](*args)
                    break
                except ValueError:
                    print('Only integer is allowed! Try again! ')
            continue