import operator

if __name__ == '__main__':
    integers = []
    while True:
        try:
            integers.extend(map(int, input().split()))
            if len(integers) == 2 and all(value in range(1, 1001) for value in integers):
                break
        except ValueError:
            print('Only integer is allowed! ')
            
    n, m = integers
    arr = []
    for _ in range(n):
        result = []
        while True:
            values = map(int, input().split())
            result.extend(values) 
            if len(result) == m and all(num in range(1001) for num in result):
                break 
        arr.append(result)
    
    while True:
        k = int(input())
        if k in range(m):
            break
    
    for value in sorted(arr, key=operator.itemgetter(k)):
        print(*value)

                
