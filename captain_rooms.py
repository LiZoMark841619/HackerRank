from collections import Counter

K = int(input())
room_number_list = list(map(int, input().split()))
counting_numbers = Counter(room_number_list)
for room_number in counting_numbers:
    if counting_numbers[room_number] == 1:
        print(room_number)