import numpy as np 

def make_a_matrix(number_of_rows_and_columns=int(input())) -> np.array:
    N = number_of_rows_and_columns
    my_2D_list = []    
    for _ in range(N):
        my_1D_list = []
        while len(my_1D_list) != N:
            my_1D_list.extend(map(int, input().split()))
        my_2D_list.append(my_1D_list)
    my_matrix = np.array(my_2D_list)
    return my_matrix


if __name__ == '__main__':
    A = make_a_matrix()
    B = make_a_matrix()
    print(np.dot(A, B))