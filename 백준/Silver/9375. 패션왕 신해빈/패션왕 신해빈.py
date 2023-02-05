from collections import Counter
import sys
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    T=int(input())
    arr=[]
    
    for j in range(T):
        a,b=map(str,input().rstrip().split(' '))
        arr.append(b)
    CNT=1
    Result=Counter(arr)
    
    for key in Result:
        CNT*=Result[key]+1
        
    print(CNT-1)