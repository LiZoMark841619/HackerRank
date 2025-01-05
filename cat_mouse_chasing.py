import sys

def catAndMouse(x, y, z):
    return 'Cat B' if abs(z - y) < abs(z - x) else 'Mouse C' if abs(z - y) == abs(z - x) else 'Cat A'

if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input())

    for _ in range(q):
        x, y, z = map(int, input().split())
        result = catAndMouse(x, y, z)
        fptr.write(str(result) + '\n')