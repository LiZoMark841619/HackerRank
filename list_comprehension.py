from itertools import product

def possible_coordinates(x: int, y: int, z: int, n: int) -> list:
    alter_result_new = product(range(x+1), range(y+1), range(z+1))
    alter_final = filter(lambda x: sum(x) != n, alter_result_new)
    return [list(value) for value in alter_final]

if __name__ == '__main__':
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    print(possible_coordinates(x, y, z, n))

# Previous solution
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result_new = [[x_value, y_value, z_value] for z_value in range(z+1) for y_value in range(y+1) for x_value in range(x+1)]
# result_new.sort()
# final = [value for value in result_new if sum(value) != n]
# print(result_new)
# print(final)
