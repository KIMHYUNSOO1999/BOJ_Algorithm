import sys
input=sys.stdin.readline 

N,Money=map(int,input().split(" "))

coins=[]
for _ in range(N):
    coins.append(int(input()))
    
CNT=0

for row in coins[::-1]:
    if(Money==0): break
    CNT+=Money//row
    Money%=row
    
print(CNT)
        
        