import sys
input = sys.stdin.readline

n = int(input())
for idx in range(1,n+1):
    
    tmp = list(map(int,input().split()))
    arr = tmp[1:len(tmp)]
    arr.sort()

    gap = 0
    for i in range(len(arr)-1):
        tmp = abs(arr[i+1]-arr[i])
        if gap <= tmp:
            gap = tmp

    print('Class' , idx)
    print(f'Max {max(arr)}, Min {min(arr)}, Largest gap {gap}')   