import sys
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    
    tmp=input()
    arr=set(map(int,input().rstrip().split(' ')))
    
    tmp=input()
    a=list(map(int,input().rstrip().split(' ')))

    for word in a:
        if word in arr:
            print(1)
        else:
            print(0)