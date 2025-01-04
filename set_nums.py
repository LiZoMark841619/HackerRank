numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])
integers = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for num in integers:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1
print(happiness)