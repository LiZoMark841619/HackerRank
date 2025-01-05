x = int(input())
y = int(input())
z = int(input())
n = int(input())

result_new = [[x_value, y_value, z_value] for z_value in range(z+1) for y_value in range(y+1) for x_value in range(x+1)]
result_new.sort()
final = [value for value in result_new if sum(value) != n]
print(result_new)
print(final)

from itertools import product

alter_result_new = list(product(range(x+1), range(y+1), range(z+1)))
alter_final = list(filter(lambda x: sum(list(x)) != n, alter_result_new))
print(alter_result_new)
print(alter_final)