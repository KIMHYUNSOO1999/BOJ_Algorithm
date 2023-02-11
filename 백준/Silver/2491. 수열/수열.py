import sys
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().rstrip().split(' ')))

dp_1=[0]*N
dp_2=[0]*N

for i in range(N-1):
    if arr[i]<=arr[i+1]:
        dp_1[i]+=dp_1[i-1]+1
    else:
        dp_1[i]=0
        
    if arr[i]>=arr[i+1]:
        dp_2[i]+=dp_2[i-1]+1
    else:
        dp_2[i]=0
        
if max(dp_1)+1 < max(dp_2)+1:
    print(max(dp_2)+1)
else:
    print(max(dp_1)+1)