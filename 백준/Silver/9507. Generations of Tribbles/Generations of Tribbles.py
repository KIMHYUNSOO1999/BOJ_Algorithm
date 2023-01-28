dp=[0]*68

for i in range(68):
    if i<2:
        dp[i]=1
    elif i==2:
        dp[i]=2
    elif i==3:
        dp[i]=4
    else:
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]
        
N=int(input())

for _ in range(N):
    print(dp[int(input())])