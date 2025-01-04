import array

def countApplesAndOranges(s, t, a, apples_or_oranges):
    validation_range, tree_loc = range(s, t+1), a
    print(sum(1 for location in apples_or_oranges if tree_loc + location in validation_range))

if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    
    apples, oranges = map(int, input().split()), map(int, input().split())
    apples, oranges = array.array('q', apples), array.array('q', oranges)
    
    countApplesAndOranges(s, t, a, apples)
    countApplesAndOranges(s, t, b, oranges)