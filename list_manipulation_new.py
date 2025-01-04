def take_actions(L:list) -> dict:
    return {'print': lambda: print(L),
            'remove': L.remove,
            'append': L.append,
            'sort': L.sort,
            'pop': L.pop,
            'reverse': L.reverse,
            'insert': L.insert}

if __name__ == '__main__':
    L = []
    N = int(input())
    actions = take_actions(L)

    for _ in range(N):
        command_input = input().split()
        command = command_input[0]
        args = map(int, command_input[1:])
        actions[command](*args)