import sys
from itertools import product

def getMoneySpent(keyboards: list, drives: list, b: int):
    result = list(product(keyboards, drives))
    printing_result = [sum(list(value)) for value in result if sum(list(value)) <= b]      
    return max(printing_result, default=-1)
            
if __name__ == '__main__':
    fptr = sys.stdout
    b, n, m = map(int, input().split())
    keyboards = map(int, input().rstrip().split())
    drives = map(int, input().rstrip().split())
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()