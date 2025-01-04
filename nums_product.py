from itertools import product

first_list = map(int, input().split())
second_list = map(int, input().split())

first_list = list(first_list)
second_list = list(second_list)

print(*list(product(first_list, second_list)))