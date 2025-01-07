def fib_making(n: int) -> list:
    fiblist = [0, 1]
    i = 0
    while fiblist[-1] < n:
        fiblist.append(fiblist[i] + fiblist[i+1])
        i += 1
    return fiblist
        
def isFibo(fibolist: list, n: int) -> None:
    if n == fibolist[-1]:
        print('IsFibo')
    else:
        print('IsNotFibo')
        
if __name__ == '__main__':
    for _ in range(int(input())):
        number = int(input())
        fibo = fib_making(number)
        isFibo(fibo, number)