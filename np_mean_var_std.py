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
    print(np.mean(my_array, axis=1))
    print(np.var(my_array, axis=0))
    std_no_axis = np.std(my_array)
    str_std = str(std_no_axis).split('.')
    if len(str_std[1]) > 11:
        print(f'{std_no_axis:.11f}')
    else:
        print(std_no_axis)