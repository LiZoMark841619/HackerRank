x, k = map(int, input().split())
P = input().strip().split()
P = [list(value) for value in P]

for value in P:
    if 'x' in value:
        idx = value.index('x')
        value.pop(idx)
        value.insert(idx, str(x))
        
result = [''.join(value) for value in P]
    
fin = ''
for value in result:
    fin += ''.join(value)

print(True if eval(fin) == k else False)