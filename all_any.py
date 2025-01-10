def get_valid_number(min_value: int, max_value: int) -> int:
    while True:
        value = input(f'Set a value between {min_value} and {max_value}! ')
        try:
            value = int(value)
            if value in range(min_value, max_value+1):
                return value
            print(f'Out of range! Please enter a number between {min_value} and {max_value}! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')
            
def get_integer_values(expected_length: int) -> list:        
    some_list: list[int] = []
    while True:
        values = input(f'Create a list! Its length must be {expected_length}! ').split()
        if len(values) != expected_length:
            print(f'Invalid number of elements! It must contain {expected_length} values! Try again! ')
            continue
        try:
            int_values = list(map(int, values))
            some_list = int_values
            return some_list
        except ValueError:
            print('All elements must be integers! Try again! ')
            
def check_conditions(values: list[int]) -> bool:
    first_conditional = all(num >= 0 for num in values)
    second_conditional = any(str(value) == str(value)[::-1] for value in values)
    return all([first_conditional, second_conditional])

def main():
    N = get_valid_number(1, 10)
    values = get_integer_values(N)
    print(check_conditions(values))

if __name__ == '__main__':
    main()