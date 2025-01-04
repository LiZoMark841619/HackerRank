if __name__ == '__main__':
    from collections import defaultdict
    n, m = map(int, input().split())
    dict_positions = defaultdict(list)
    for i in range(n):
        value = input()
        dict_positions[value].append(i+1)
    print(dict_positions)
    for _ in range(m):
        value = input()
        if value in dict_positions:
            print(*dict_positions[value])
        else:
            print(-1)