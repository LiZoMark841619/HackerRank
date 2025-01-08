import operator

class Valids:
    number_of_instances = 0
    
    def set_a_list(self, length: int, min_value: int, max_value: int) -> None:
        Valids.number_of_instances += 1
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
    valids = Valids()
    valids.set_a_list(2, 1, 1000)
    n, m = valids.get_a_list()
    arr = []
    for _ in range(n):
        valids.set_a_list(m, 0, 1000)
        result = valids.get_a_list()
        arr.append(result)
    
    while True:
        k = int(input())
        if k in range(m):
            break
    
    for value in sorted(arr, key=operator.itemgetter(k)):
        print(*value)