import numpy as np

def get_valid_list():
    while True:
        try:
            numbers = list(map(int, input().split()))
            if len(numbers) == 9:
                return numbers
            else:
                print('Your list must have {} values! Try again! ')
        except ValueError:
            print('Invalid value! Try again with integers! ')

def reshape_array(some_list: list, rows: int, columns: int) -> np.array:
    return np.reshape(np.array(some_list), (rows, columns))
    
if __name__ == '__main__':
    numbers = get_valid_list()
    print(reshape_array(numbers, 3, 3))