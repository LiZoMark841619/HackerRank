from itertools import combinations

def divisibleSumPairs(k, ar):
    combination_list = list(combinations(ar, 2))
    final = [value for value in combination_list if (value[0] + value[1]) % k == 0]
    return len(final)    
        
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    while True:
        ar = list(map(int, input().rstrip().split()))
        if len(ar) == n: 
            result = divisibleSumPairs(k, ar)
            print(result)
            break
        else:
            print('Invalid list length! Try again! ')