N=int(input())
nums_list=list(map(int,input().split(' ')))

dp=[0]*N
dp[0]=nums_list[0]

for i in range(1,N):
    dp[i]=max(nums_list[i],dp[i-1]+nums_list[i])
    
print(max(dp))