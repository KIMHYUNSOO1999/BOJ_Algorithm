from collections import deque

import sys
input=sys.stdin.readline 

a=deque()
N=int(input())

for _ in range(N):
    
    command=input().split()
    
    if command[0]=="push_front":
        a.appendleft(command[1])
    elif command[0]=='push_back':
        a.append(command[1])
    elif command[0]=='pop_front':
        if len(a)>0:
            print(a[0])    
            a.popleft()
        else:
            print('-1')
    elif command[0]=='pop_back':
        if len(a)>0:
            print(a[len(a)-1])    
            a.pop()
        else:
            print('-1')
    elif command[0]=='size':
        print(len(a))
    elif command[0]=='empty':
        if len(a)>0:
            print('0')
        else:
            print('1')
    elif command[0]=='front':
        if len(a)>0:
            print(a[0])    
        else:
            print('-1')
    elif command[0]=='back':
        if len(a)>0:
            print(a[len(a)-1])    
        else:
            print('-1')
