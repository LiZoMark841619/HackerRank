def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    for num in arr:
        if num > 0: positives += 1
        elif num < 0: negatives += 1
        else: zeros += 1
    return [positives, negatives, zeros]
    
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = plusMinus(arr)
    for num in res:
        print(f'{num/len(arr):.6f}')