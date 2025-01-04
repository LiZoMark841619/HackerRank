def set_length() -> int:
    while True:
        try:
            length = int(input('Enter the lenght of your list: '))
            if 0 < length < 10: return length
            print('Length of list must be under 10 and above 0! Try again! ')
        except ValueError: print('Only integer (from 1 to 10) is allowed! Try again! ')

def make_a_list(length: int) -> list:
    return [input(f'Enter the {_+1}# value of your list: ') for _ in range(length)]

def take_actions(some_list: list) -> dict:
        return {'remove':lambda:some_list.remove(input('Enter a value to remove: ')),
                'insert':lambda:some_list.insert(int(input('Index where to insert: ')), input('New value to insert: ')),
                'reverse':lambda:some_list.reverse(),
                'sort':lambda:some_list.sort(),
                'append':lambda:some_list.append(input('New value to add: ')),
                'print':lambda:print(some_list),
                'pop':lambda:some_list.pop()}

if __name__ == '__main__':
    list_length_setting = set_length()
    test_one = make_a_list(length=list_length_setting)
    print('The original list is: ')
    print(test_one)
    for _ in range(int(input('How many commands would you like to give? Enter a number! '))):
        command = input('Enter a command from [insert, reverse, sort, append, print, pop, remove] options! ')
        test = take_actions(test_one)
        test[command]()
        print(test_one)