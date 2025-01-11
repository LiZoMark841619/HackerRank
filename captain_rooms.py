from collections import Counter

def find_captain_room(room_number_list: list) -> int:
    counting_numbers = Counter(room_number_list)
    for room_number, count in counting_numbers.items():
        if count== 1:
            return room_number

if __name__ == '__main__':
    while True:
        K = int(input('Enter the number of people in each group! '))
        if K in range(1, 1000):
            break
    
    while True:
        room_number_list = list(map(int, input().split()))
        if len(room_number_list) % K == 1:
            captain_room = find_captain_room(room_number_list)
            print(f"{captain_room} ")
            break
        print('The given room number list is not valid! Please try again! ')