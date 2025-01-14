# def sort_odd_before_even(somelist: list) -> tuple[list, list]:
#     result, odd_numbers, even_numbers = [], [], []
#     for value in somelist:
#         try: 
#             value = int(value)
#             if value % 2 == 0: even_numbers.append(str(value))
#             else: odd_numbers.append(str(value))
#         except ValueError: result.append(value)
#     odd_numbers.sort()
#     even_numbers.sort()
#     odd_numbers.extend(even_numbers)
#     result.extend(odd_numbers)
#     return result

# if __name__ == '__main__':
#     S = input()
#     list_string = list(S)
#     list_string.sort()
#     list_string.sort(key=str.isupper)
#     list_string.sort(key=str.isdigit)
#     print(''.join(sort_odd_before_even(list_string)))

#better solution after understanding the problem
from typing import TypeVar

function = TypeVar('function')

def get_valid_input(prompt: str, condition: function) -> str:
    while True:
        values = input(prompt)
        if condition(values):
            return values

def sorting_strings(some_string: str) -> str:
    some_string = list(some_string)   
    some_string.sort(key=lambda x: (x.isdigit(), x.isupper(), x))
    only_numbers = list(filter(lambda x: x.isdigit(), some_string))
    only_letters = [char for char in some_string if char.isalpha()]
    odds = list(filter(lambda x: int(x) % 2 == 1, only_numbers))
    evens = [num for num in only_numbers if num not in odds]
    return ''.join(only_letters+odds+evens)
    
if __name__ == '__main__':
    S = get_valid_input('', lambda x: len(x) in range(1, 1000))
    print(sorting_strings(S))
