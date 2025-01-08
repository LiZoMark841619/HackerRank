if __name__ == '__main__':
    N = 0
    while True:
        value = input('Set a value between 1 and 1000! ')
        try:
            int_value = int(value)
            if int_value in range(1, 1001):
                N += int_value
                break
            else:
                print('Out of range! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')
            
    some_list: list[int] = []
    while True:
        values = input().split()
        try:
            int_values = map(int, values)
            if len(list(int_values)) == N:
                some_list.extend(int_values)
                break
        except ValueError:
            print('Only integer is allowed! Try again! ')

    first_conditional = all(num >= 0 for num in some_list)
    values = [list(str(value)) for value in some_list]
    reversed_values = [list(reversed(value)) for value in values]
    second_conditional = any(values[i] == reversed_values[i] for i in range(len(values)))
    print(all([first_conditional, second_conditional]))