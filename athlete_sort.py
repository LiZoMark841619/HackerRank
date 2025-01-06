import operator

if __name__ == '__main__':
    n = 0
    m = 0
    while (n and m) not in range(1, 1001):
        integers = list(map(int, input().split()))
        n += integers[0]
        m += integers[1]
            
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