import sys
from itertools import product

def make_a_list(lenght: int, min_val: int, max_val: int) -> list:
        some_list = []
        while True:
            values = input().split()
            try:
                vals = list(map(int, values))
                if len(vals) == lenght and all(value in range(min_val, max_val+1) for value in vals):
                    some_list.extend(vals)
                    return some_list
            except ValueError:
                print('Only integer is allowed! ')
                
def getMoneySpent(keyboards: list, drives: list, b: int)-> int:
    return max((s for s in (sum(pair) for pair in product(keyboards, drives)) if s <= b), default=-1)
            
if __name__ == '__main__':
    fptr = sys.stdout
    while True:
        try:
            b, n, m = map(int, input().split())
            if b in range(1, 10**6+1) and (n and m) in range(1, 1001):
                break
        except ValueError:
            print('Only integer is allowed! Try again!')
    
    keyboards = make_a_list(n, 1, 10**6)
    drives = make_a_list(m, 1, 10**6)
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()