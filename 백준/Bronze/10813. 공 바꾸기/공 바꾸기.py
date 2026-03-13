import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr =  [i+1 for i in range(N)]

for _ in range(M):
    left, right = map(int,input().split())
    left, right = left-1, right-1

    tmp=arr[left]
    arr[left]=arr[right]
    arr[right]=tmp
   
print(*arr)