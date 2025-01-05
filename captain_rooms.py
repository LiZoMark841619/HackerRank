from collections import Counter

if __name__ == '__main__':
    K = int(input())
    room_number_list = map(int, input().split())
    counting_numbers = Counter(room_number_list)
    for room_number in counting_numbers:
        if counting_numbers[room_number] == 1:
            print(room_number)