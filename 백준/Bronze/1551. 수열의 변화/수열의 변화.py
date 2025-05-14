import sys
input = sys.stdin.readline

_, t = map(int,input().split())
arr=list(map(int, input().split(',')))

for _ in range(t):

    tmp = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1):
        tmp[i] = arr[i+1] - arr[i]

    arr = tmp

if t == 0:
    tmp = arr
    
print(','.join(map(str, tmp[:len(arr)-t])))