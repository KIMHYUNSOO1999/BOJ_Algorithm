N= 1000 - int(input())

money=[500,100,50,10,5,1]

CNT_sum=0

for i in range(6):
    if N==0: break
        
    CNT=N//money[i]
    N-=(CNT*money[i])
    CNT_sum+=CNT

print(CNT_sum)