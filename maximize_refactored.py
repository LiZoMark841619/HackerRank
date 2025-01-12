from itertools import product

def get_valid_input(prompt, condition):
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if condition(values):
                return values
            else:
                print("Invalid input. Try again!")
        except ValueError:
            print("Only integers are allowed! Try again!")

def main():
    K, M = get_valid_input("Enter the values of K and M: ", lambda x: len(x) == 2 and 1 <= x[0] <= 7 and 1 <= x[1] <= 1000)

    result = []
    for i in range(K):
        values = get_valid_input(f"Enter the list of integers for list {i+1}: ", lambda x: len(x) > 1 and 1 <= x[0] <= 7 and all(1 <= v <= 10**9 for v in x[1:]))
        result.append(values[1:])

    max_value = max(sum(x**2 for x in combo) % M for combo in product(*result))
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()