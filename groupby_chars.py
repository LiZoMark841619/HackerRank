from itertools import groupby

if __name__ == '__main__':
    while True:
        S = input()
        if len(S) in range(1, 10**4+1):
            break
            
    final = [(len(list(v)), int(k)) for k, v in groupby(S)]
    print(*final, sep=' ')