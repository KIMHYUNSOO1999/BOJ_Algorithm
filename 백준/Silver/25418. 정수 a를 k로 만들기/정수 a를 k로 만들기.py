import sys
input = sys.stdin.readline

A,K= map(int, input().rstrip().split())

CNT=0

while True:
    if A==K: break
        
    if (K%2==0) and (K>=(A*2)):
        K//=2
        CNT+=1
    else:
        K-=1
        CNT+=1

print(CNT)