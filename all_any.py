if __name__ == '__main__':
    while True:
        value = input('Set a value between 1 and 1000! ')
        try:
            value = int(value)
            if value in range(1, 1001):
                break
            else:
                print('Out of range! Please enter a number between 1 and 1000! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')
            
    some_list: list[int] = []
    while True:
        values = input(f'Create a list! Its length must be {value}! ').split()
        if len(values) != value:
            print(f'Invalid number of elements! It must contain {value} values! Try again! ')
            continue
        try:
            int_values = list(map(int, values))
            some_list = int_values
            break
        except ValueError:
            print('All elements must be integers! Try again! ')

    first_conditional = all(num >= 0 for num in some_list)
    values = [list(str(value)) for value in some_list]
    reversed_values = [list(reversed(str_value)) for str_value in values]
    second_conditional = any(values[i] == reversed_values[i] for i in range(len(values)))
    print(all([first_conditional, second_conditional]))