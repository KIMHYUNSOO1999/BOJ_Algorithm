import sys
input = sys.stdin.readline

dp=[0]*80

dp[0]=1
dp[1]=1

for i in range(2,len(dp)):
    dp[i]=dp[i-1]+dp[i-2]
    
N=int(input())

Result=(dp[N-1]*2)+((dp[N-1]+dp[N-2])*2)

if N==1:
    print(4)
else:    
    print(Result)