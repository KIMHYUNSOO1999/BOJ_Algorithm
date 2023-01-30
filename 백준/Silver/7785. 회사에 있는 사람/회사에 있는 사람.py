import sys
input=sys.stdin.readline

arr={}
N=int(input())

for _ in range(N):
    a,b=map(str,input().rstrip().split(' '))
    if b == 'enter':
        arr[a] = 'enter'
    else:
        if arr[a]:
            del arr[a]
    
for word in sorted(arr, reverse=True):
    print(word)