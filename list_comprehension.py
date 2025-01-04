x = int(input())
y = int(input())
z = int(input())
n = int(input())

result_new = [[x_value, y_value, z_value] for z_value in range(z+1) for y_value in range(y+1) for x_value in range(x+1)]
result_new.sort()
final = [value for value in result_new if sum(value) != n]
print(final)