import sys
from collections import defaultdict

def make_def_and_rev_dicts(n: int)-> tuple[dict, dict]:
    
    pages_in_a_book = defaultdict(tuple)
    page = 0
    
    for idx in range(n+1):
        pages_in_a_book[idx] += (page, page + 1)
        page += 2
        
    for key in pages_in_a_book.copy():
        if pages_in_a_book[key][0] > n:
            del pages_in_a_book[key]
        
    reversed_book = dict(reversed(list(pages_in_a_book.items())))
    
    return pages_in_a_book, reversed_book

def search_key(D: dict, p: int, straight_or_reversed: str=None):
    result = []
    for key in D:
        if p in D[key]:
            if straight_or_reversed is None:
                result.append(key)
            elif straight_or_reversed == 'reverse':
                result.append(max(D.keys()) - key)
    return result

if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    p = int(input().strip())
    result = make_def_and_rev_dicts(n)
    one_val, two_val = search_key(result[0], p), search_key(result[-1], p, 'reverse')
    result = [one_val, two_val]
    result = min(result)
    fptr.write(str(result[0]) + '\n')
    fptr.close()
