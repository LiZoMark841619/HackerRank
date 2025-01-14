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
def sorting_strings(some_string: str) -> str:
    some_string = list(S)   
    some_string.sort(key=lambda x: (x.isdigit(), x.isupper(), x))
    only_numbers = list(filter(lambda x: x.isdigit(), some_string))
    only_letters = list(filter(lambda x: x.isalpha(), some_string))
    odds = list(filter(lambda x: int(x) % 2 == 1, only_numbers))
    evens = list(filter(lambda x: int(x) % 2 == 0, only_numbers))
    return ''.join(only_letters+odds+evens)
    
if __name__ == '__main__':
    S = input()
    print(sorting_strings(S))