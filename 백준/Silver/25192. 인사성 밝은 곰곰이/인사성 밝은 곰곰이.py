import sys
input = sys.stdin.readline

n = int(input().rstrip())

visited = set()
result = 0

for _ in range(n):

    order = input().rstrip()
    
    if order == 'ENTER':
        visited = set()
    else:
        if order not in visited:
            visited.add(order)
            result+=1

print(result)
            