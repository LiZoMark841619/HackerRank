from collections import Counter
            
def get_valid_string() -> str:
    s = ''
    while len(s) not in range(3, 10**4) and len(set(s)) <= 3:
        s += input()
    return s

if __name__ == '__main__':
    s = list(get_valid_string())
    s.sort()
    most_common = Counter(s).most_common()[:3]
    for val in most_common:
        print(*val)