import sys
from itertools import combinations

def getMoneySpent(keyboards, drives, b):
    keyboard_list = list(combinations(keyboards, 1))
    drive_list = list(combinations(drives, 1))
    
    result = []
    for val_1 in keyboard_list:
        for val_2 in drive_list:
            result.append(val_1+val_2)
    
    printing_result = []      
    for value in result:
        final = sum(list(value))
        if final <= b:
            printing_result.append(final)
    printing_result.sort()
    return printing_result[-1] if printing_result else -1
            
if __name__ == '__main__':
    fptr = sys.stdout
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
