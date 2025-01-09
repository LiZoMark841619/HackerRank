import sys
from itertools import product

def make_a_list(lenght: int, min_val: int, max_val: int) -> list:
        some_list = []
        while True:
            values = input(f'Setup a list! Length must be {lenght}! Values between: {min_val}-{max_val}: ').split()
            try:
                vals = list(map(int, values))
                if len(vals) != lenght:
                    print('Invalid length! Try again! ')
                elif all(value in range(min_val, max_val+1) for value in vals):
                    some_list.extend(vals)
                    return some_list
                else:
                    print('You value(s) is/are out of range! ')
            except ValueError:
                print('Only integer is allowed! ')
                
def getMoneySpent(keyboards: list, drives: list, b: int)-> int:
    return max((s for s in (sum(pair) for pair in product(keyboards, drives)) if s <= b), default=-1)
            
if __name__ == '__main__':
    fptr = sys.stdout
    while True:
        values = input('Setup budget, and the number of keyboards and drives: ').split()
        try:
            bnm = list(map(int, values))
            if len(bnm) != 3:
                print('Your list is invalid! It must have 3 values! ')
            elif bnm[0] not in range(1, 10**6+1) or bnm[1] not in range(1, 1001) or bnm[2] not in range(1, 1001):
                print('Your values are out of range! Try again! ')
            else:
                break
        except ValueError:
            print('Only integer is allowed! Try again!')
    
    keyboards = make_a_list(bnm[1], 1, 10**6)
    drives = make_a_list(bnm[2], 1, 10**6)
    moneySpent = getMoneySpent(keyboards, drives, bnm[0])
    fptr.write(str(moneySpent) + '\n')
    fptr.close()