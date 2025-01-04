import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())
    my_list = []
    for _ in range(N):
        result = []
        while len(result) != M:
            result.extend(map(int, input().split()))
        my_list.append(result)
    my_array = np.array(my_list)
    sum_0_axis = np.sum(my_array, axis=0)
    prod_no_axis = np.prod(sum_0_axis)
    print(prod_no_axis)        