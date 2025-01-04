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
    min_1_axis = np.min(my_array, axis=1)
    max_no_axis = np.max(min_1_axis)
    print(max_no_axis)