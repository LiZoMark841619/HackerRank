import operator

class Valid:
    number_of_instances = 0
    
    def set_a_number(self, min_value: int, max_value: int) -> None:
        Valid.number_of_instances += 1
        while True:
            try:
                valid_number = int(input())
                if valid_number in range(min_value, max_value+1):
                    self.__number = valid_number
                    return
                else:
                    print(f'Out of range! Enter a number from {min_value} to {max_value}! ')
            except ValueError:
                print('Invalid value! Only integer is allowed! ')
    
    def get_a_number(self) -> int:
        return self.__number
    
    def set_a_list(self, length: int, min_value: int, max_value: int) -> None:
        Valid.number_of_instances += 1
        final = []
        while True:
            values = input().split()
            try:
                result = list(map(int, values))
                conditional = (value in range(min_value, max_value+1) for value in result)
                if len(result) == length and all(conditional):
                    final.extend(result)
                    self.__final = final
                    return
                elif len(result) != length:
                    print(f'Your list is invalid! The number of values must be {length}! ')
                else:
                    print(f'Your values are out of range! They must be between {min_value} and {max_value}')
            except ValueError:
                print('Only integer is allowed! Try again! ')

    def get_a_list(self) -> list:
        return self.__final

if __name__ == '__main__':
    valids = Valid()
    valids.set_a_list(2, 1, 1000)
    n, m = valids.get_a_list()
    
    arr = []
    for _ in range(n):
        valids.set_a_list(m, 0, 1000)
        result = valids.get_a_list()
        arr.append(result)
    
    valids.set_a_number(0, m)
    k = valids.get_a_number()
    
    for value in sorted(arr, key=operator.itemgetter(k)):
        print(*value)