import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]

for _ in range(M):
    
    i, j = map(int, input().split())
    left = i - 1
    right = j - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
print(*arr)