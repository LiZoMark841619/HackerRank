import sys

def findPoint(px: int, py: int, qx: int, qy: int) -> tuple[int, int]:
    result = (qx + (qx-px), qy + (qy-py))
    return result
    
if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    for _ in range(n):
        px, py, qx, qy = map(int, input().split())
        result = findPoint(px, py, qx, qy)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
