from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    
    input()
    N, M = map(int,input().split())
    arrS=sorted(list(map(int,input().split())))
    arrB=sorted(list(map(int,input().split())))
    
    arrS=deque(arrS)
    arrB=deque(arrB)
    
    s = arrS[0]
    b = arrB[0]
    
    while arrS and arrB:
        s = arrS[0]
        b = arrB[0]
        
        if s == b:
            arrB.popleft() 
        elif s > b:
            arrB.popleft()
        else:
            arrS.popleft()
    
    if len(arrS)!=0:
        print('S')
    elif len(arrB)!=0:
        print('B')
    else:
        print('C')
