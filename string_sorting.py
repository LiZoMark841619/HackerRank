def sort_odd_before_even(somelist: list) -> tuple[list, list]:
    result, odd_numbers, even_numbers = [], [], []
    for value in somelist:
        try: 
            value = int(value)
            if value % 2 == 0: even_numbers.append(str(value))
            else: odd_numbers.append(str(value))
        except ValueError: result.append(value)
    odd_numbers.sort()
    even_numbers.sort()
    odd_numbers.extend(even_numbers)
    result.extend(odd_numbers)
    return result

if __name__ == '__main__':
    S = input()
    list_string = list(S)
    list_string.sort()
    list_string.sort(key=str.isupper)
    list_string.sort(key=str.isdigit)
    print(''.join(sort_odd_before_even(list_string)))