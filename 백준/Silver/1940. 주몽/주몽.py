import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int,input().strip().split()))

arr.sort()
start, end = 0, len(arr)-1
result = 0

while start < end:
    
    tmp = arr[start]+arr[end]

    if tmp < m:
        start +=1
    elif tmp > m:
        end-=1
    else:
        result+=1
        start+=1
        end-=1

print(result)