while(True):
    N=input()
    if 0<=int(N)<=99: break
        
        
if int(N)<10:
    N=N+'0'
else:
    N=N

count=0
check=0
second_cycle=''
x=N[0]
y=N[1]

while(True):
    
    if second_cycle == N and check==1: break
    
    first_cycle=str(int(x)+int(y))
    
    first_cycle_temp=y+first_cycle
    
    if int(first_cycle_temp)>100:
    
        second_cycle=first_cycle_temp[0]+first_cycle_temp[2]
        x=second_cycle[0]
        y=second_cycle[1]
        
    else:
        second_cycle=y+str(first_cycle)
        x=second_cycle[0]
        y=second_cycle[1]
    
    count+=1
    check=1
    
print(count)