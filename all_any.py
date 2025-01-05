if __name__ == '__main__':
    N = 0
    while N not in range(1, 101):
        N += int(input())
            
    some_list: list[int] = []
    while len(some_list) != N: 
        some_list.extend(map(int, input().split()))

    first_conditional = all(num >= 0 for num in some_list)
    values = [list(str(value)) for value in some_list]
    reversed_values = [list(reversed(value)) for value in values]
    second_conditional = any(values[i] == reversed_values[i] for i in range(len(values)))
    print(all([first_conditional, second_conditional]))