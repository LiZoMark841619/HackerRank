from collections import Counter
import sys

def migratoryBirds(arr):
    count_types_of_birds = Counter(arr)
    max_value = max(count_types_of_birds.values())
    return min([key for key in count_types_of_birds if count_types_of_birds[key] == max_value])

if __name__ == '__main__':
    fptr = sys.stdout
    arr_count = int(input().strip())
    while True:
        arr = list(map(int, input().rstrip().split()))
        if len(arr) == arr_count:
            result = migratoryBirds(arr)
            fptr.write(str(result) + '\n')
            fptr.close()
            break
        print('You have more birds than free space! Try again! ')