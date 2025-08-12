import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))

visited = [False for _ in range(n)]
arrSort = sorted(arr)
result = [0] * n

order = 0
for val in arrSort:
    for i in range(n):
        if arr[i] == val and not visited[i]:
            visited[i] = True
            result[i] = order
            order += 1
            break  
            
print(*result)