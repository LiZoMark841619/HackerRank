def valid_float_number(string: str) -> bool:
    
    if string.count('.') != 1 or string[-1] == '.':
        return False
    else:
        if string[0] == '.':
            return True if string[1:].isdigit() else False

        elif string.startswith('+') or string.startswith('-'):
            if string[1] == '.':
                return True if string[2:].isdigit() else False
            else:
                return True if string[1:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit() else False

        elif string[0].isdigit():
            return True if string[:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit() else False
        else:
            return False
        
if __name__ == '__main__':
    T = 0
    while T not in range(1, 10):
        T += int(input())
    for _ in range(T):
        print(valid_float_number(input()))