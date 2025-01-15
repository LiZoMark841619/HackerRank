import numpy as np
from typing import TypeVar

function = TypeVar('function')
def get_valid_number(prompt: str, condition: function) -> int:
    while True:
        try:
            N = int(input(prompt))
            if condition(N): return N
            else: print('The input is invalid! Try again! ')
        except ValueError: print('You need to input an integer! Try again! ')

def make_a_square_matrix(prompt: str) -> np.array:
    N = get_valid_number(prompt, lambda x: x in range(1, 6))
    my_2D_list = []    
    for _ in range(N):
        while True:
            try:
                row = list(map(int, input('Enter the values of the row: ').split()))
                if len(row) == N:
                    my_2D_list.append(row)
                    break
                else: print(f'You need to input {N} integers! Try again! ')
            except ValueError: print('You need to input integers! Try again! ')
    return np.array(my_2D_list)

if __name__ == '__main__':
    A = make_a_square_matrix('Enter the number of rows and columns of matrix A: ')
    while True:
        B = make_a_square_matrix('Enter the number of rows and columns of matrix B: ')
        if A.shape[1] == B.shape[0]: break
        else: print('The number of columns of matrix A must be equal to the number of rows of matrix B! Try again! ')
    print(np.dot(A, B))