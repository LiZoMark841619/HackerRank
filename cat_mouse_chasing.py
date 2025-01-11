def catAndMouse(x, y, z):
    return 'Cat B' if abs(z - y) < abs(z - x) else 'Mouse C' if abs(z - y) == abs(z - x) else 'Cat A'

if __name__ == '__main__':
    q = int(input('Enter the number of queries: '))

    for _ in range(q):
        x, y, z = map(int, input('Enter the position of Cat A, Cat B and the Mouse: ').split())
        result = catAndMouse(x, y, z)
        print(result)