from collections import Counter

def migratoryBirds(arr):
    count_types_of_birds = Counter(arr)
    max_value = max(count_types_of_birds.values())
    return min(key for key in count_types_of_birds if count_types_of_birds[key] == max_value)

if __name__ == '__main__':
    arr_count = int(input("Enter the number of bird sightings: ").strip())
    while True:
        arr = list(map(int, input("Enter the bird types: ").rstrip().split()))
        if len(arr) == arr_count:
            result = migratoryBirds(arr)
            print(result)
            break
        print("The number of bird types entered does not match the expected count. Try again!")