import numpy as np 

def make_a_vector(number_of_rows_and_columns=2) -> np.array:
    N = number_of_rows_and_columns
    my_1D_list = []    
    while len(my_1D_list) != N:
        my_1D_list.extend(map(int, input().split()))
    my_vector = np.array(my_1D_list)
    return my_vector

if __name__ == '__main__':
    A = make_a_vector()
    B = make_a_vector()
    print(np.inner(A, B))
    print(np.outer(A, B))