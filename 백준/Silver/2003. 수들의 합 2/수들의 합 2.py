import sys
input = sys.stdin.readline

N,M=map(int,input().rstrip().split(' '))

arr=list(map(int,input().rstrip().split(' ')))

start=0
end=1
CNT=0

while end<=N and start<=end:
    tmp=arr[start:end]
    total=sum(tmp)
    
    if total==M:
        CNT+=1
        end+=1
    elif total<M:
        end+=1
    else:
        start+=1
        
print(CNT)