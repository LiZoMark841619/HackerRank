from collections import Counter

def get_valid_number(prompt: str, min_val:int, max_val:int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val < value < max_val:
                return value
            print('Invalid number! Try again! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')

def get_a_valid_list(length_of_list: int, min_value: int, max_value: int) -> list:
    while True:
        try:
            values = list(map(int, input(f'Enter a value from ({min_value} to {max_value}) {length_of_list} times! ').split()))
            if len(values) != length_of_list:
                print(f'Invalid number of elements! It must contain {length_of_list} values! Try again!')
                continue
            else:
                for value in values:
                    idx = values.index(value)
                    if value not in range(min_value, max_value+1):
                        while True:
                            new_value = int(input(f'Enter a new value from {min_value} and {max_value} instead of {value}! '))
                            if new_value in range(min_value, max_value+1):
                                values[idx] = new_value
                                break
                return values
        except ValueError: print('ValueError! Only integer is allowed! ')

if __name__ == '__main__':
    number_of_shoes = get_valid_number('Number of shoes (1-9): ', 0, 10)
    shoe_sizes = get_a_valid_list(length_of_list=number_of_shoes, min_value=1, max_value=10)
    number_of_customs = get_valid_number('Number of customers in the shop (1-9): ', 0, 10)
    shoes_available = Counter(shoe_sizes)
    customs_inquiries = {}
    total_revenue = 0
    for _ in range(number_of_customs):
        size, price = map(int, input('Preferred size and selling price! ').split())
        customs_inquiries[size] = price
        if size in list(shoes_available.keys()) and shoes_available[size] != 0:
            total_revenue += price
            shoes_available[size] -= 1
    print(total_revenue)