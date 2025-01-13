import re

def valid_float_number(string: str) -> bool:
    
    if string.count('.') != 1 or string[-1] == '.':
        return False
    
    elif string[0] == '.':
        return bool(string[1:].isdigit())

    elif string.startswith('+') or string.startswith('-'):
        if string[1] == '.':
            return bool(string[2:].isdigit())
        else:
            return bool(string[1:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit())

    elif string[0].isdigit():
        return bool(string[:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit())
    else:
        return False

def valid_float_number_alter(string: str) -> bool:
    pattern = r'^[+-]?\d*\.\d+$'
    return bool(re.match(pattern, string))

if __name__ == '__main__':
    while True:
        T = int(input())
        if T in range(1, 10):
            break
    for _ in range(T):
        print(valid_float_number_alter(input()))