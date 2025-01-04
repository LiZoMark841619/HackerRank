import sys

def catAndMouse(x, y, z):
    return 'Cat B' if abs(z - y) < abs(z - x) else 'Mouse C' if abs(z - y) == abs(z - x) else 'Cat A'

if __name__ == '__main__':
    fptr = sys.stdout
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        fptr.write(str(result) + '\n')