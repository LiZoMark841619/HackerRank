from itertools import combinations

def divisibleSumPairs(k: int, ar: list) -> len:
    combination_list = combinations(ar, 2)
    return len(list(filter(lambda x: (x[0]+x[1])% k == 0, combination_list)))  
        
if __name__ == '__main__':
    n = 0
    k = 0
    while n not in range(2, 101) or k not in range(1, 101):
        inputs = input().split()
        try:
            n += int(inputs[0])
            k += int(inputs[1])
        except ValueError:
            print('Only integer is allowed! Try again! ')
        
    while True:
        try:
            ar = list(map(int, input().split()))
            if len(ar) == n and all(value in range(1, 101) for value in ar): 
                print(divisibleSumPairs(k, ar))
                break
            else:
                print('Invalid list length! Try again! ')
        except ValueError:
            print('Only integer is allowed! Try again! ')