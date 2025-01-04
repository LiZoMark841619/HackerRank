import sys

def actions_(some_set: set)-> dict:
    return {'pop': some_set.pop, 'remove': some_set.remove, 'discard': some_set.discard}

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    actions = actions_(s)
    for _ in range(N):
        while True:
            command_input = input().split()
            if command_input[0] in actions.keys():
                command = command_input[0]
                args = map(int, command_input[1:])
                actions[command](*args)
                break
            else:
                print(f'Invalid command! Try again from {list(actions.keys())} ')
        
    result = sum(list(s))
    fptr = sys.stdout
    fptr.write(str(s))
    fptr.write('\n')
    fptr.write(str(result))