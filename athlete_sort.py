import operator

class Valid:
    number_of_instances = 0
    
    def set_a_number(self, prompt: str, min_value: int, max_value: int, input_value: str = None) -> None:
        Valid.number_of_instances += 1
        while True:
            try:
                valid_number = int(input_value if input_value is not None else input(prompt))
                if valid_number in range(min_value, max_value+1):
                    self.__number = valid_number
                    return
                else:
                    print(f'Out of range! Enter a number from {min_value} to {max_value}! ')
            except ValueError:
                print('Invalid value! Only integer is allowed! ')
    
    def get_a_number(self) -> int:
        return self.__number
    
    def set_a_list(self, prompt: str, length: int, min_value: int, max_value: int, input_values: str = None) -> None:
        Valid.number_of_instances += 1
        while True:
            values = (input_values if input_values is not None else input(prompt)).split()
            try:
                result = list(map(int, values))
                if len(result) == length and all(min_value <= value <= max_value for value in result):
                    self.__final = result
                    return
                elif len(result) != length:
                    print(f'Your list is invalid! The number of values must be {length}! ')
                else:
                    print(f'Your values are out of range! They must be between {min_value} and {max_value}')
            except ValueError:
                print('Only integer is allowed! Try again! ')

    def get_a_list(self) -> list:
        return self.__final

    def set_a_string(self, prompt, *args) -> None:
        while True:
            value = input(prompt)
            if value in args:
                self.__string = value
                return
            
    def get_a_string(self) -> str:
        return self.__string
    
class Process:
    def __init__(self) -> None:
        self.valid = Valid()
    
    def ask_to_play(self) -> bool:
        self.valid.set_a_string('Do you want to play? (yes/no) ', 'yes', 'no')
        return self.valid.get_a_string() == 'yes'
    
    def settings(self):
        self.valid.set_a_number('Enter the number of athletes (2-1000): ', 1, 1000)
        self.athletes = self.valid.get_a_number()
        self.valid.set_a_number('Enter the number of attributes (0-1000): ', 1, 1000)
        self.attributes = self.valid.get_a_number()
        self.arr = []
        for _ in range(self.athletes):
            self.valid.set_a_list('Enter the attributes! ', self.attributes, 0, 1000)
            self.arr.append(self.valid.get_a_list())
        self.valid.set_a_number('Enter the attribute to sort by! ', 0, self.attributes-1)
        self.k = self.valid.get_a_number()
        
    def main(self):
        self.settings()
        for value in sorted(self.arr, key=operator.itemgetter(self.k)):
            print(*value)

if __name__ == '__main__':
    process = Process()
    if process.ask_to_play():
        process.main()