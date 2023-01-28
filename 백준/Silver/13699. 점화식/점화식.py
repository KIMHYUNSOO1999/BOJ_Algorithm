dp = [0] * 36

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5
 
for i in range(4,36):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]

N = int(input())

print(dp[N])