sum=0
nums=[]

N=int(input())
nums=list(map(int,input().split(" ")))

for row in nums:
    sum+=(row/max(nums))*100
    
print(sum/N)