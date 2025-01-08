integers = []

while True:
    try:
        values = map(int, input().split())
        integers.extend(values)
        if len(integers) == 2:
            break
    except ValueError:
        print('Only integer is allowed! Try again! ')