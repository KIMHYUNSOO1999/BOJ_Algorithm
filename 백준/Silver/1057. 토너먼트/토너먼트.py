N,A,B=map(int,input().split())

CNT=0

while A!=B:
    
    A-=A//2
    B-=B//2
    CNT+=1
    
print(CNT)
    