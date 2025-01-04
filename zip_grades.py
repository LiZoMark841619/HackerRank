if __name__ == '__main__':
    while True:
        try:
            N, X = map(int, input().split())
            if N and X in range(0, 100):
                break
        except ValueError:
            print('Invalid value! Only integer is allowed! ')
    result = []   
    for _ in range(X):
        grades = []
        while len(grades) != N:
            grades.extend(map(float, input().split()))
        result.append(grades)
    for value in list(zip(*result)):
        print(f'{sum(value)/len(value):.1f}')
    