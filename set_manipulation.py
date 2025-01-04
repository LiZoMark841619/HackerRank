def take_actions(some_set: set) -> dict:
    return {
        'intersection_update': some_set.intersection_update,
        'update': some_set.update,
        'symmetric_difference_update': some_set.symmetric_difference_update,
        'difference_update': some_set.difference_update
        }
    
def update_set(some_set: set, length: int) -> set:
    while len(some_set) != length:
        some_set.update(set(map(int, input().split())))
    return some_set

if __name__ == '__main__':
    number_of_elements, A = int(input()), set()
    update_A = update_set(A, number_of_elements)
    actions = take_actions(update_A)
    options = actions.keys()

    N = int(input())
    for _ in range(N):
        while True:
            command_input = input().split()
            if command_input[0] in options:
                command = command_input[0]
                length = int(command_input[-1])
                new_set = set()
                update_new_set = update_set(new_set, length)
                actions[command](update_new_set)
                break
    print(sum(list(update_A)))