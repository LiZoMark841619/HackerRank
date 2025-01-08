def countApplesAndOranges(s: int, t: int, a: int, apples_or_oranges: map) -> None:
    print(sum(1 for location in apples_or_oranges if a + location in range(s, t+1)))

if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    
    apples, oranges = map(int, input().split()), map(int, input().split())
    
    countApplesAndOranges(s, t, a, apples)
    countApplesAndOranges(s, t, b, oranges)